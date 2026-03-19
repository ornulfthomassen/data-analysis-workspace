"""End-to-end pipeline orchestration for training, scoring, and device enrichment.

Supports both full pipeline runs and individual step execution with
intermediate results saved to parquet files for inspection.
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path

import pandas as pd

from device_prediction import bq_client
from device_prediction.config import Settings
from device_prediction.device_agent import enrich_devices_batch, find_missing_devices
from device_prediction.device_history import build_device_change_history
from device_prediction.encoding import (
    build_preprocessing_pipeline,
    get_model_feature_columns,
)
from device_prediction.extract import extract_subscription_history
from device_prediction.features import build_feature_matrix
from device_prediction.model import (
    evaluate_model,
    load_model,
    predict_survival_curves,
    save_model,
    split_data,
    train_model,
)
from device_prediction.statistics import (
    compute_device_model_stats,
    compute_market_stats,
    compute_subscriber_stats,
)
from device_prediction.target import construct_survival_target_vectorized

logger = logging.getLogger(__name__)

DEFAULT_DATA_DIR = Path("data/intermediate")


def _save_intermediate(df: pd.DataFrame, name: str, data_dir: Path) -> Path:
    """Save intermediate DataFrame to parquet and print summary."""
    data_dir.mkdir(parents=True, exist_ok=True)
    path = data_dir / f"{name}.parquet"
    df.to_parquet(path, index=False)
    logger.info("Saved %s: %d rows, %d cols → %s", name, len(df), len(df.columns), path)
    return path


def _load_intermediate(name: str, data_dir: Path) -> pd.DataFrame:
    """Load intermediate DataFrame from parquet."""
    path = data_dir / f"{name}.parquet"
    if not path.exists():
        raise FileNotFoundError(
            f"Intermediate file not found: {path}\n"
            f"Run the previous step first to generate it."
        )
    df = pd.read_parquet(path)
    logger.info("Loaded %s: %d rows, %d cols ← %s", name, len(df), len(df.columns), path)
    return df


# ── Individual steps ─────────────────────────────────────────────────────

def step_extract(
    cfg: Settings,
    mode: str = "train",
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Step 1: Extract subscription history from BigQuery."""
    logger.info("=== Step: Extract subscription history (mode=%s) ===", mode)
    df = extract_subscription_history(cfg, mode=mode)
    _save_intermediate(df, f"subscription_hist_{mode}", data_dir)
    print(f"\nExtracted {len(df):,} rows, {len(df.columns)} columns")
    print(f"Subscribers: {df['main_number_sk'].nunique():,}")
    print(f"Period range: {df['period_month_date'].min()} → {df['period_month_date'].max()}")
    print(f"Devices: {df['device_marketing_name'].nunique():,} unique models")
    return df


def step_device_history(
    cfg: Settings,
    mode: str = "train",
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Step 2: Build cleaned device change history."""
    logger.info("=== Step: Build device change history ===")
    sub_hist = _load_intermediate(f"subscription_hist_{mode}", data_dir)
    df = build_device_change_history(sub_hist, cfg)
    _save_intermediate(df, f"device_history_{mode}", data_dir)
    print(f"\nDevice history: {len(df):,} device spells")
    print(f"Subscribers: {df['main_number_sk'].nunique():,}")
    n_with_change = df["days_since_previous_device"].notna().sum()
    print(f"Device transitions: {n_with_change:,}")
    if n_with_change > 0:
        print(f"Median days between changes: {df['days_since_previous_device'].median():.0f}")
    return df


def step_statistics(
    cfg: Settings,
    mode: str = "train",
    data_dir: Path = DEFAULT_DATA_DIR,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Step 3: Compute statistics at three levels."""
    logger.info("=== Step: Compute statistics ===")
    device_hist = _load_intermediate(f"device_history_{mode}", data_dir)

    sub_stats = compute_subscriber_stats(device_hist)
    mkt_stats = compute_market_stats(device_hist)
    dev_stats = compute_device_model_stats(device_hist)

    _save_intermediate(sub_stats, f"subscriber_stats_{mode}", data_dir)
    _save_intermediate(mkt_stats, f"market_stats_{mode}", data_dir)
    _save_intermediate(dev_stats, f"device_model_stats_{mode}", data_dir)

    print(f"\nSubscriber stats: {len(sub_stats):,} rows ({sub_stats['main_number_sk'].nunique():,} subscribers)")
    print(f"Market stats: {len(mkt_stats):,} months")
    print(f"Device model stats: {len(dev_stats):,} entries ({dev_stats['device_marketing_name'].nunique():,} models)")
    return sub_stats, mkt_stats, dev_stats


def step_features(
    cfg: Settings,
    mode: str = "train",
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Step 4: Build feature matrix by joining all data sources."""
    logger.info("=== Step: Build feature matrix ===")
    sub_hist = _load_intermediate(f"subscription_hist_{mode}", data_dir)
    sub_stats = _load_intermediate(f"subscriber_stats_{mode}", data_dir)
    mkt_stats = _load_intermediate(f"market_stats_{mode}", data_dir)
    dev_stats = _load_intermediate(f"device_model_stats_{mode}", data_dir)

    logger.info("Loading device features from BigQuery")
    device_features = bq_client.read_table(
        cfg.bigquery.device_features_table, cfg.bigquery.project_id
    )
    _save_intermediate(device_features, "device_features", data_dir)

    df = build_feature_matrix(
        sub_hist, sub_stats, mkt_stats, dev_stats, device_features, cfg, mode=mode
    )
    _save_intermediate(df, f"feature_matrix_{mode}", data_dir)

    print(f"\nFeature matrix: {len(df):,} rows, {len(df.columns)} columns")
    print(f"Subscribers: {df['main_number_sk'].nunique():,}")
    n_numeric = df.select_dtypes(include="number").shape[1]
    print(f"Numeric features: {n_numeric}")
    return df


def step_target(
    cfg: Settings,
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Step 5: Construct survival target (train only)."""
    logger.info("=== Step: Construct survival target ===")
    feature_matrix = _load_intermediate("feature_matrix_train", data_dir)
    sub_stats = _load_intermediate("subscriber_stats_train", data_dir)

    df = construct_survival_target_vectorized(feature_matrix, sub_stats, cfg)
    _save_intermediate(df, "feature_matrix_with_target", data_dir)

    n_events = int(df["event"].sum())
    n_censored = len(df) - n_events
    print(f"\nSurvival target constructed: {len(df):,} observations")
    print(f"Events (device change): {n_events:,} ({100*n_events/len(df):.1f}%)")
    print(f"Censored: {n_censored:,} ({100*n_censored/len(df):.1f}%)")
    print(f"Median duration (events): {df.loc[df['event']==1, 'duration_months'].median():.1f} months")
    print(f"Median duration (censored): {df.loc[df['event']==0, 'duration_months'].median():.1f} months")
    return df


def step_encode(
    cfg: Settings,
    mode: str = "train",
    model_path: Path = Path("models/latest"),
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Step 6: Run preprocessing/encoding pipeline."""
    logger.info("=== Step: Preprocessing (mode=%s) ===", mode)

    if mode == "train":
        df = _load_intermediate("feature_matrix_with_target", data_dir)
    else:
        df = _load_intermediate("feature_matrix_score", data_dir)

    pipeline_path = model_path / "pipeline.joblib"

    if mode == "train":
        model_path.mkdir(parents=True, exist_ok=True)
        df, pipeline = build_preprocessing_pipeline(
            df, cfg, mode="fit", pipeline_path=pipeline_path
        )
    else:
        df, pipeline = build_preprocessing_pipeline(
            df, cfg, mode="transform", pipeline_path=pipeline_path
        )

    _save_intermediate(df, f"encoded_{mode}", data_dir)

    feature_cols = get_model_feature_columns(df)
    print(f"\nEncoded matrix: {len(df):,} rows, {len(df.columns)} columns")
    print(f"Model features: {len(feature_cols)}")
    return df


def step_train(
    cfg: Settings,
    model_path: Path = Path("models/latest"),
    data_dir: Path = DEFAULT_DATA_DIR,
) -> dict:
    """Step 7: Train and evaluate survival model."""
    logger.info("=== Step: Train model ===")
    df = _load_intermediate("encoded_train", data_dir)

    feature_cols = get_model_feature_columns(df)
    X_train, X_test, y_train, y_test = split_data(df, feature_cols, cfg)

    model, train_metrics = train_model(X_train, y_train, cfg)
    test_metrics = evaluate_model(model, X_test, y_test)

    all_metrics = {**train_metrics, **test_metrics}

    # Load pipeline if exists
    pipeline_path = model_path / "pipeline.joblib"
    pipeline = None
    if pipeline_path.exists():
        import joblib
        pipeline = joblib.load(pipeline_path)

    save_model(model, pipeline, model_path, metadata={
        "metrics": all_metrics,
        "feature_columns": feature_cols,
        "n_train": len(X_train),
        "n_test": len(X_test),
    })

    print(f"\n=== Training Metrics ===")
    for k, v in all_metrics.items():
        print(f"  {k}: {v}")
    print(f"\nModel saved to {model_path}")
    return all_metrics


def step_predict(
    cfg: Settings,
    model_path: Path = Path("models/latest"),
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Step 8: Predict survival curves and write to BigQuery."""
    logger.info("=== Step: Predict ===")
    df = _load_intermediate("encoded_score", data_dir)

    model, _, metadata = load_model(model_path)
    feature_cols = metadata.get("feature_columns", get_model_feature_columns(df))
    feature_cols = [c for c in feature_cols if c in df.columns]

    predictions = predict_survival_curves(model, df[feature_cols])

    # Attach identifiers
    id_cols = ["main_number_sk", "period_month_date", "device_producername"]
    for col in ["customer_sk_user", "current_device", "device_marketing_name"]:
        if col in df.columns:
            id_cols.append(col)

    output = pd.concat([
        df[[c for c in id_cols if c in df.columns]].reset_index(drop=True),
        predictions.reset_index(drop=True),
    ], axis=1)
    output["score_date"] = datetime.now().strftime("%Y-%m-%d")

    _save_intermediate(output, "predictions", data_dir)

    print(f"\nPredictions: {len(output):,} rows")
    print(f"Columns: {list(output.columns)}")
    print(f"\nSample (top 5):")
    print(output.head().to_string())

    return output


def step_write_scores(
    cfg: Settings,
    data_dir: Path = DEFAULT_DATA_DIR,
) -> None:
    """Step 9: Write predictions to BigQuery."""
    logger.info("=== Step: Write scores to BigQuery ===")
    output = _load_intermediate("predictions", data_dir)

    month_suffix = datetime.now().strftime("%Y%m")
    table_id = f"{cfg.bigquery.score_output_dataset}.{cfg.bigquery.score_output_prefix}_{month_suffix}"
    bq_client.write_dataframe(output, table_id, cfg.bigquery.project_id)

    print(f"\nWrote {len(output):,} predictions to {table_id}")


# ── Full pipeline runs (unchanged) ──────────────────────────────────────

def run_training_pipeline(
    cfg: Settings,
    model_output_path: str | Path = "models/latest",
    skip_enrichment: bool = False,
    data_dir: Path = DEFAULT_DATA_DIR,
) -> dict:
    """Full training pipeline: enrich → extract → clean → features → train → save."""
    model_output_path = Path(model_output_path)

    if not skip_enrichment:
        run_device_enrichment(cfg)

    step_extract(cfg, mode="train", data_dir=data_dir)
    step_device_history(cfg, mode="train", data_dir=data_dir)
    step_statistics(cfg, mode="train", data_dir=data_dir)
    step_features(cfg, mode="train", data_dir=data_dir)
    step_target(cfg, data_dir=data_dir)
    step_encode(cfg, mode="train", model_path=model_output_path, data_dir=data_dir)
    return step_train(cfg, model_path=model_output_path, data_dir=data_dir)


def run_scoring_pipeline(
    cfg: Settings,
    model_path: str | Path = "models/latest",
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """Full scoring pipeline: extract → clean → features → predict → write to BQ."""
    model_path = Path(model_path)

    step_extract(cfg, mode="score", data_dir=data_dir)
    step_device_history(cfg, mode="score", data_dir=data_dir)
    step_statistics(cfg, mode="score", data_dir=data_dir)
    step_features(cfg, mode="score", data_dir=data_dir)
    step_encode(cfg, mode="score", model_path=model_path, data_dir=data_dir)
    step_predict(cfg, model_path=model_path, data_dir=data_dir)
    step_write_scores(cfg, data_dir=data_dir)

    return _load_intermediate("predictions", data_dir)


def run_device_enrichment(cfg: Settings) -> pd.DataFrame:
    """Standalone device enrichment pipeline."""
    logger.info("=== Device enrichment ===")
    missing = find_missing_devices(cfg)

    if len(missing) == 0:
        logger.info("No missing devices to enrich")
        return pd.DataFrame()

    logger.info("Found %d devices to enrich", len(missing))
    result = enrich_devices_batch(missing, cfg)
    logger.info("Enrichment complete: %d devices enriched", len(result))
    return result

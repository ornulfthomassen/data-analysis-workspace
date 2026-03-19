"""Survival model training, evaluation, prediction, and persistence.

Uses scikit-survival GradientBoostingSurvivalAnalysis as the default model.
Outputs survival probability curves at configurable time horizons.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from device_prediction.config import Settings

logger = logging.getLogger(__name__)

# Default time points (months) at which to predict survival probabilities
DEFAULT_TIME_POINTS = [1, 2, 3, 6, 9, 12, 18, 24]


def make_survival_target(df: pd.DataFrame) -> np.ndarray:
    """Convert DataFrame duration_months/event columns to scikit-survival structured array."""
    return np.array(
        [(bool(e), float(d)) for e, d in zip(df["event"], df["duration_months"])],
        dtype=[("event", bool), ("duration", float)],
    )


def split_data(
    df: pd.DataFrame,
    feature_columns: list[str],
    cfg: Settings,
) -> tuple[pd.DataFrame, pd.DataFrame, np.ndarray, np.ndarray]:
    """Split into train/test sets with stratification on event indicator.

    Returns (X_train, X_test, y_train, y_test).
    """
    X = df[feature_columns]
    y = make_survival_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=cfg.model.test_size,
        random_state=cfg.model.random_state,
        stratify=df["event"],
    )

    logger.info(
        "Split: %d train (%d events), %d test (%d events)",
        len(X_train), y_train["event"].sum(),
        len(X_test), y_test["event"].sum(),
    )
    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame,
    y_train: np.ndarray,
    cfg: Settings,
) -> tuple[Any, dict]:
    """Train a survival analysis model.

    Returns (trained_model, metrics_dict).
    """
    from sksurv.ensemble import GradientBoostingSurvivalAnalysis

    model = GradientBoostingSurvivalAnalysis(
        n_estimators=cfg.model.n_estimators,
        learning_rate=cfg.model.learning_rate,
        max_depth=cfg.model.max_depth,
        random_state=cfg.model.random_state,
    )

    logger.info(
        "Training %s (n_estimators=%d, lr=%.3f, depth=%d)",
        cfg.model.type, cfg.model.n_estimators,
        cfg.model.learning_rate, cfg.model.max_depth,
    )
    model.fit(X_train, y_train)
    logger.info("Training complete")

    metrics = _compute_metrics(model, X_train, y_train, label="train")
    return model, metrics


def evaluate_model(
    model: Any,
    X_test: pd.DataFrame,
    y_test: np.ndarray,
) -> dict:
    """Evaluate model on held-out test data."""
    return _compute_metrics(model, X_test, y_test, label="test")


def predict_survival_curves(
    model: Any,
    X: pd.DataFrame,
    time_points: list[float] | None = None,
) -> pd.DataFrame:
    """Predict survival probabilities at specified time points.

    Returns DataFrame with columns:
    - risk_score: overall risk ranking (higher = sooner expected change)
    - median_survival_months: predicted median time to device change
    - prob_change_within_{t}m: 1 - S(t) for each time point
    """
    if time_points is None:
        time_points = DEFAULT_TIME_POINTS

    # Risk scores (higher = more likely to change sooner)
    risk_scores = model.predict(X)

    # Survival functions
    surv_fns = model.predict_survival_function(X)

    results = {"risk_score": risk_scores}

    # Extract probabilities at each time point
    for t in time_points:
        probs = []
        for fn in surv_fns:
            # S(t) = probability of NOT having changed by time t
            # P(change within t) = 1 - S(t)
            if t <= fn.x[-1]:
                surv_prob = fn(t)
            else:
                surv_prob = fn(fn.x[-1])
            probs.append(1.0 - surv_prob)
        results[f"prob_change_within_{t}m"] = probs

    # Median survival time
    medians = []
    for fn in surv_fns:
        below_50 = fn.x[fn.y <= 0.5]
        if len(below_50) > 0:
            medians.append(float(below_50[0]))
        else:
            medians.append(float(fn.x[-1]))
    results["median_survival_months"] = medians

    return pd.DataFrame(results, index=X.index)


def save_model(
    model: Any,
    pipeline: Any,
    path: str | Path,
    metadata: dict | None = None,
) -> None:
    """Save model, preprocessing pipeline, and metadata."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, path / "model.joblib")
    if pipeline is not None:
        joblib.dump(pipeline, path / "pipeline.joblib")

    meta = {
        "saved_at": datetime.now().isoformat(),
        "model_type": type(model).__name__,
        **(metadata or {}),
    }
    with open(path / "metadata.json", "w") as f:
        json.dump(meta, f, indent=2, default=str)

    logger.info("Model saved to %s", path)


def load_model(path: str | Path) -> tuple[Any, Any, dict]:
    """Load model, pipeline, and metadata from directory."""
    path = Path(path)

    model = joblib.load(path / "model.joblib")

    pipeline_path = path / "pipeline.joblib"
    pipeline = joblib.load(pipeline_path) if pipeline_path.exists() else None

    meta_path = path / "metadata.json"
    metadata = {}
    if meta_path.exists():
        with open(meta_path) as f:
            metadata = json.load(f)

    logger.info("Model loaded from %s (%s)", path, metadata.get("model_type", "unknown"))
    return model, pipeline, metadata


def _compute_metrics(model: Any, X: pd.DataFrame, y: np.ndarray, label: str) -> dict:
    """Compute survival model evaluation metrics."""
    from sksurv.metrics import concordance_index_censored

    risk_scores = model.predict(X)
    c_index = concordance_index_censored(y["event"], y["duration"], risk_scores)

    metrics = {
        f"{label}_concordance_index": float(c_index[0]),
        f"{label}_concordant": int(c_index[1]),
        f"{label}_discordant": int(c_index[2]),
        f"{label}_n_samples": len(X),
        f"{label}_n_events": int(y["event"].sum()),
    }

    logger.info(
        "%s metrics: C-index=%.4f (n=%d, events=%d)",
        label, c_index[0], len(X), y["event"].sum(),
    )
    return metrics

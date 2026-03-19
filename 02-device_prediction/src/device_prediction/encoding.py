"""Feature preprocessing pipeline using sklearn.

Replaces the 20+ hardcoded SQL CASE statements for one-hot encoding
with a dynamic, data-driven sklearn pipeline that handles unseen
categories gracefully.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from device_prediction.config import Settings

logger = logging.getLogger(__name__)

# Columns that should never be features (identifiers and raw text)
ID_COLUMNS = [
    "main_number_sk", "customer_sk_user", "period_month_date",
    "device_release_date", "current_device_first_use_date",
    "period_month", "stat_first_use_month",
]

# Text/categorical columns that need encoding or dropping
CATEGORICAL_ENCODE_COLUMNS = ["device_producername"]
CATEGORICAL_DROP_COLUMNS = [
    "device_marketing_name", "current_device", "device_name",
    "manufacturer", "context_summary", "generation",
    "device_group",
]
CATEGORICAL_PASSTHROUGH = [
    "device_category", "device_series_annual", "display_type",
]

# Survival target columns
TARGET_COLUMNS = ["duration_months", "event"]


def get_feature_split(df: pd.DataFrame) -> dict[str, list[str]]:
    """Categorize columns into their roles.

    Returns dict with keys: 'numeric', 'encode', 'passthrough_cat',
    'id', 'drop', 'target'.
    """
    all_cols = set(df.columns)

    ids = [c for c in ID_COLUMNS if c in all_cols]
    targets = [c for c in TARGET_COLUMNS if c in all_cols]
    encode = [c for c in CATEGORICAL_ENCODE_COLUMNS if c in all_cols]
    drop = [c for c in CATEGORICAL_DROP_COLUMNS if c in all_cols]
    passthrough_cat = [c for c in CATEGORICAL_PASSTHROUGH if c in all_cols]

    known = set(ids + targets + encode + drop + passthrough_cat)
    numeric = sorted(c for c in all_cols - known if df[c].dtype in ("float64", "int64", "Float64", "Int64"))

    return {
        "numeric": numeric,
        "encode": encode,
        "passthrough_cat": passthrough_cat,
        "id": ids,
        "drop": drop,
        "target": targets,
    }


def build_preprocessing_pipeline(
    df: pd.DataFrame,
    cfg: Settings,
    mode: Literal["fit", "transform"],
    pipeline_path: str | Path | None = None,
) -> tuple[pd.DataFrame, Pipeline | None]:
    """Build or apply the feature preprocessing pipeline.

    fit mode: Fit OneHotEncoder on training data, save pipeline, return transformed df.
    transform mode: Load fitted pipeline, apply to new data.
    """
    split = get_feature_split(df)

    if mode == "fit":
        pipeline = _build_encoder(df, split)
        transformed = _apply_pipeline(df, pipeline, split)

        if pipeline_path:
            path = Path(pipeline_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            joblib.dump(pipeline, path)
            logger.info("Saved preprocessing pipeline to %s", path)

        return transformed, pipeline

    else:  # transform
        if not pipeline_path:
            raise ValueError("pipeline_path required in transform mode")

        pipeline = joblib.load(pipeline_path)
        logger.info("Loaded preprocessing pipeline from %s", pipeline_path)
        transformed = _apply_pipeline(df, pipeline, split)
        return transformed, pipeline


def _build_encoder(df: pd.DataFrame, split: dict) -> ColumnTransformer:
    """Build sklearn ColumnTransformer with OneHotEncoder for categorical columns."""
    transformers = []

    if split["encode"]:
        ohe = OneHotEncoder(
            sparse_output=False,
            handle_unknown="infrequent_if_exist",
            min_frequency=0.005,
        )
        transformers.append(("onehot", ohe, split["encode"]))

    if split["passthrough_cat"]:
        cat_ohe = OneHotEncoder(
            sparse_output=False,
            handle_unknown="infrequent_if_exist",
            min_frequency=0.01,
        )
        transformers.append(("cat_onehot", cat_ohe, split["passthrough_cat"]))

    ct = ColumnTransformer(
        transformers=transformers,
        remainder="drop",
        verbose_feature_names_out=True,
    )
    ct.fit(df)
    logger.info("Fitted encoder with %d transformers", len(transformers))
    return ct


def _apply_pipeline(
    df: pd.DataFrame,
    pipeline: ColumnTransformer,
    split: dict,
) -> pd.DataFrame:
    """Apply the fitted pipeline and reassemble the full DataFrame."""
    # Transform encoded columns
    encoded_array = pipeline.transform(df)
    encoded_cols = pipeline.get_feature_names_out()
    encoded_df = pd.DataFrame(encoded_array, columns=encoded_cols, index=df.index)

    # Combine: numeric + encoded + id + target
    keep_cols = split["numeric"] + split["id"] + split["target"]
    keep_cols = [c for c in keep_cols if c in df.columns]

    result = pd.concat([df[keep_cols].reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)
    return result


def get_model_feature_columns(df: pd.DataFrame) -> list[str]:
    """Return the list of columns to use as model features (excludes IDs and targets)."""
    exclude = set(ID_COLUMNS + TARGET_COLUMNS)
    return [c for c in df.columns if c not in exclude]

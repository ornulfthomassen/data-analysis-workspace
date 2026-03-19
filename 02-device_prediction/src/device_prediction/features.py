"""Feature matrix assembly.

Joins subscription history with all statistics levels and device features
to produce the final feature matrix for modeling. Replaces the large
JOIN query from the POC SQL (lines 354-537 of device_change_abt.sql).
"""

from __future__ import annotations

import logging
from datetime import date
from typing import Literal

import numpy as np
import pandas as pd

from device_prediction.config import Settings

logger = logging.getLogger(__name__)


def build_feature_matrix(
    subscription_hist: pd.DataFrame,
    subscriber_stats: pd.DataFrame,
    market_stats: pd.DataFrame,
    device_model_stats: pd.DataFrame,
    device_features: pd.DataFrame,
    cfg: Settings,
    mode: Literal["train", "score"],
) -> pd.DataFrame:
    """Assemble the full feature matrix by joining all data sources.

    Joins:
    1. subscription_hist + subscriber_stats (subscriber + device + period)
    2. + market_stats (13-month rolling window)
    3. + device_model_stats (device model + month)
    4. + device_features (LLM-enriched device specs)

    Then adds seasonal and computed features.
    """
    logger.info("Building feature matrix (mode=%s)", mode)

    df = _join_subscriber_stats(subscription_hist, subscriber_stats)
    df = _join_market_stats(df, market_stats, cfg)
    df = _join_device_model_stats(df, device_model_stats)
    df = _join_device_features(df, device_features)
    df = _add_computed_features(df)
    df = _add_seasonal_features(df)

    logger.info("Feature matrix: %d rows, %d columns", len(df), len(df.columns))
    return df


def _join_subscriber_stats(
    sub_hist: pd.DataFrame,
    sub_stats: pd.DataFrame,
) -> pd.DataFrame:
    """Join subscription history with per-subscriber device statistics.

    Matches on main_number_sk + device_marketing_name where the
    observation period >= device first use date.
    """
    sub_hist = sub_hist.copy()
    sub_hist["period_month"] = pd.to_datetime(sub_hist["period_month_date"]).dt.to_period("M").dt.to_timestamp()

    # Subset of subscriber stats relevant for the join
    stats_cols = [
        "main_number_sk", "device_marketing_name", "device_first_use_date",
        "device_release_date", "days_since_previous_device",
        "days_first_use_after_release", "med_days_since_previous_device",
        "last_device_rank",
    ]
    stats = sub_stats[[c for c in stats_cols if c in sub_stats.columns]].copy()
    stats["stat_first_use_month"] = pd.to_datetime(stats["device_first_use_date"]).dt.to_period("M").dt.to_timestamp()

    # Join: subscriber + device + period >= first_use
    merged = sub_hist.merge(
        stats,
        on=["main_number_sk", "device_marketing_name"],
        how="left",
        suffixes=("", "_stat"),
    )

    # Filter: observation period must be >= device first use
    if "stat_first_use_month" in merged.columns:
        merged = merged[
            merged["period_month"] >= merged["stat_first_use_month"]
        ].copy()

    # Aggregate per observation (subscriber + period + device)
    group_cols = [c for c in sub_hist.columns if c in merged.columns]
    agg_dict = {}

    if "device_first_use_date_stat" in merged.columns:
        agg_dict["device_first_use_date_stat"] = "min"
    if "days_since_previous_device" in merged.columns:
        agg_dict["days_since_previous_device"] = "mean"
    if "days_first_use_after_release" in merged.columns:
        agg_dict["days_first_use_after_release"] = "min"
    if "med_days_since_previous_device" in merged.columns:
        agg_dict["med_days_since_previous_device"] = "mean"

    if agg_dict:
        agg_result = merged.groupby(group_cols, dropna=False).agg(**{
            k: pd.NamedAgg(column=k, aggfunc=v) for k, v in agg_dict.items()
        }).reset_index()
        # Rename aggregated columns
        rename_map = {
            "days_since_previous_device": "avg_change_days",
            "med_days_since_previous_device": "med_change_days",
            "device_first_use_date_stat": "current_device_first_use_date",
        }
        agg_result.rename(
            columns={k: v for k, v in rename_map.items() if k in agg_result.columns},
            inplace=True,
        )
        return agg_result

    return merged


def _join_market_stats(
    df: pd.DataFrame,
    market_stats: pd.DataFrame,
    cfg: Settings,
) -> pd.DataFrame:
    """Join with market-level statistics using a rolling 13-month window.

    The POC uses a range join: first_use_month BETWEEN (period - 13 months)
    AND (period - 1 month). We pre-aggregate the rolling window to avoid
    a costly range join.
    """
    lookback = cfg.statistics.gen_stat_lookback_months
    ms = market_stats.sort_values("first_use_month").copy()

    # Pre-compute rolling averages over the lookback window
    ms = ms.set_index("first_use_month")
    rolled = ms.rolling(f"{lookback * 30}D", min_periods=1).mean().reset_index()
    rolled.rename(columns={"first_use_month": "period_month"}, inplace=True)

    # Shift by 1 month: stats should be from months _before_ the observation
    rolled["period_month"] = rolled["period_month"] + pd.DateOffset(months=1)

    df = df.copy()
    if "period_month" not in df.columns:
        df["period_month"] = pd.to_datetime(df["period_month_date"]).dt.to_period("M").dt.to_timestamp()

    result = pd.merge_asof(
        df.sort_values("period_month"),
        rolled.sort_values("period_month"),
        on="period_month",
        direction="backward",
    )
    return result


def _join_device_model_stats(
    df: pd.DataFrame,
    device_model_stats: pd.DataFrame,
) -> pd.DataFrame:
    """Join with per-device-model statistics.

    Matches on device_marketing_name where observation period >= stat month.
    Uses the most recent stat month available before the observation.
    """
    dms = device_model_stats.sort_values("first_use_month").copy()

    df = df.copy()
    if "period_month" not in df.columns:
        df["period_month"] = pd.to_datetime(df["period_month_date"]).dt.to_period("M").dt.to_timestamp()

    # For each device, merge_asof to get the most recent stats
    parts = []
    for device_name, group in df.groupby("device_marketing_name", sort=False):
        device_stats = dms[dms["device_marketing_name"] == device_name].copy()
        if device_stats.empty:
            parts.append(group)
            continue

        merged = pd.merge_asof(
            group.sort_values("period_month"),
            device_stats.drop(columns=["device_marketing_name"]).sort_values("first_use_month"),
            left_on="period_month",
            right_on="first_use_month",
            direction="backward",
        )
        parts.append(merged)

    if parts:
        result = pd.concat(parts, ignore_index=True)
    else:
        result = df

    if "first_use_month" in result.columns:
        result.drop(columns=["first_use_month"], inplace=True)

    return result


def _join_device_features(
    df: pd.DataFrame,
    device_features: pd.DataFrame,
) -> pd.DataFrame:
    """Join with LLM-enriched device specifications.

    Match key: UPPER(producername + ' ' + marketing_name) = UPPER(user_input)
    Uses INNER join (matching POC behavior) - devices without features are dropped.
    """
    df = df.copy()
    df["_device_key"] = (
        df["device_producername"].str.upper() + " " + df["device_marketing_name"].str.upper()
    ).str.strip()

    feats = device_features.copy()
    feats["_device_key"] = feats["user_input"].str.upper().str.strip()

    feat_cols = [
        "_device_key", "device_name", "manufacturer", "device_series_annual",
        "display_type", "context_summary", "generation", "device_series_annual_no",
        "release_year", "ram_gb", "storage_base_gb", "display_size_inches",
        "camera_rear_mp", "camera_front_mp", "launch_price_nok",
    ]
    feats = feats[[c for c in feat_cols if c in feats.columns]].drop_duplicates(
        subset=["_device_key"], keep="first"
    )

    # Cast numeric columns
    numeric_feat_cols = [
        "release_year", "ram_gb", "storage_base_gb", "display_size_inches",
        "camera_rear_mp", "camera_front_mp", "launch_price_nok",
        "device_series_annual_no",
    ]
    for col in numeric_feat_cols:
        if col in feats.columns:
            feats[col] = pd.to_numeric(feats[col], errors="coerce")

    n_before = len(df)
    result = df.merge(feats, on="_device_key", how="inner")
    result.drop(columns=["_device_key"], inplace=True)
    n_dropped = n_before - len(result)

    if n_dropped > 0:
        logger.warning(
            "Dropped %d rows (%d%%) due to missing device features",
            n_dropped,
            round(100 * n_dropped / max(n_before, 1)),
        )

    return result


def _add_computed_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add computed features derived from existing columns."""
    df = df.copy()

    period = pd.to_datetime(df["period_month_date"])
    release = pd.to_datetime(df["device_release_date"])

    # Days since device release
    df["current_device_release_days"] = (
        period.dt.to_period("M").dt.to_timestamp()
        - release.dt.to_period("M").dt.to_timestamp()
    ).dt.days

    # Days since current device first use
    if "current_device_first_use_date" in df.columns:
        first_use = pd.to_datetime(df["current_device_first_use_date"])
        df["current_device_days"] = (
            period.dt.to_period("M").dt.to_timestamp()
            - first_use.dt.to_period("M").dt.to_timestamp()
        ).dt.days
    else:
        df["current_device_days"] = np.nan

    # Ratio: current device age vs average change time
    if "avg_change_days" in df.columns:
        df["current_days_vs_avg_change_days"] = np.where(
            df["avg_change_days"].notna() & (df["avg_change_days"] > 0),
            df["current_device_days"] / df["avg_change_days"],
            np.where(
                df.get("avg_dev_change_days", pd.Series(dtype=float)).notna(),
                df["current_device_days"] / df.get("avg_dev_change_days", 1),
                np.nan,
            ),
        )
    else:
        df["current_days_vs_avg_change_days"] = np.nan

    # Cast subscription numeric columns to float
    numeric_sub_cols = [
        "net_other_fee", "no_days_mno_start", "no_days_prod_start",
        "net_discount_amount_use", "net_amount_use_cpa_3mo", "kr_mb_last3",
        "net_revenue", "net_amount_use_roam_3mo", "net_per_fee_bind_3mo",
        "no_mms_dom_last1", "kr_mb_last1", "net_use", "mb_last3",
        "net_disc_amt_use_roam_3mo", "mb_last1", "kr_mb_last2", "net_fee",
        "no_days_subs_start", "mb_last2", "net_revenue_adj_3mo",
    ]
    for col in numeric_sub_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def _add_seasonal_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add seasonal/calendar features."""
    df = df.copy()
    period = pd.to_datetime(df["period_month_date"])
    release = pd.to_datetime(df["device_release_date"])

    df["current_month_nr"] = period.dt.month
    df["current_release_month_nr"] = release.dt.month

    # Days until Christmas (next Dec 25)
    year = period.dt.year
    christmas_this_year = pd.to_datetime(
        year.astype(str) + "-12-25", format="%Y-%m-%d", errors="coerce"
    )
    christmas_next_year = pd.to_datetime(
        (year + 1).astype(str) + "-12-25", format="%Y-%m-%d", errors="coerce"
    )
    df["days_until_christmas"] = np.where(
        period > christmas_this_year,
        (christmas_next_year - period).dt.days,
        (christmas_this_year - period).dt.days,
    )

    # Days until summer (next Jun 30)
    summer_this_year = pd.to_datetime(
        year.astype(str) + "-06-30", format="%Y-%m-%d", errors="coerce"
    )
    summer_next_year = pd.to_datetime(
        (year + 1).astype(str) + "-06-30", format="%Y-%m-%d", errors="coerce"
    )
    df["days_until_summer"] = np.where(
        period > summer_this_year,
        (summer_next_year - period).dt.days,
        (summer_this_year - period).dt.days,
    )

    # Purchase month from device first use date
    if "current_device_first_use_date" in df.columns:
        df["current_purchase_month_nr"] = pd.to_datetime(
            df["current_device_first_use_date"]
        ).dt.month
    else:
        df["current_purchase_month_nr"] = np.nan

    return df

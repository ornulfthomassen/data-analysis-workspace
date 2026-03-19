"""Multi-pass device change history cleaning.

Translates the 8-step SQL cleaning pipeline (Steps 3.1-3.8 from POC SQL)
into pandas operations. Removes replacement devices, inherited/used devices,
and downgrade noise to produce a clean device timeline per subscriber.
"""

from __future__ import annotations

import logging

import pandas as pd

from device_prediction.config import Settings

logger = logging.getLogger(__name__)


def build_device_change_history(
    subscription_hist: pd.DataFrame,
    cfg: Settings,
) -> pd.DataFrame:
    """Run the full multi-pass cleaning pipeline.

    Takes raw subscription history, returns a clean device timeline with
    computed day intervals for each device transition.
    """
    logger.info("Building device change history from %d rows", len(subscription_hist))

    # Pass 1: aggregate, filter, lag, remove replacements
    df = _aggregate_device_spells(subscription_hist, cfg)
    logger.info("After aggregation: %d device spells", len(df))

    df = _add_lag_windows(df)
    df = _remove_replacement_devices(df, cfg.cleaning.min_device_usage_days)
    logger.info("After removing replacements: %d spells", len(df))

    # Remove downgrades
    df = _remove_downgrades(df)
    logger.info("After removing downgrades: %d spells", len(df))

    # Pass 2: re-lag after cleanup and compute intervals
    df = _add_lag_windows(df)
    df = _compute_day_intervals(df)

    logger.info("Device change history complete: %d rows", len(df))
    return df


def _aggregate_device_spells(df: pd.DataFrame, cfg: Settings) -> pd.DataFrame:
    """Step 3.1: Group by subscriber + device to get first/last use dates.

    Filters out devices first used > max_days_after_release after their release
    (likely inherited or second-hand devices).
    """
    grouped = (
        df.groupby(
            ["main_number_sk", "device_marketing_name", "device_producername",
             "device_category", "device_release_date"],
            dropna=False,
        )
        .agg(
            device_first_use_date=("period_month_date", "min"),
            device_last_use_date=("period_month_date", "max"),
        )
        .reset_index()
    )

    # Filter: only keep devices taken into use within N days of release
    max_days = cfg.cleaning.max_days_after_release
    grouped["days_after_release"] = (
        grouped["device_first_use_date"] - grouped["device_release_date"]
    ).dt.days
    grouped = grouped[grouped["days_after_release"] <= max_days].copy()
    grouped.drop(columns=["days_after_release"], inplace=True)

    # Sort for consistent window operations
    grouped.sort_values(
        ["main_number_sk", "device_first_use_date"], inplace=True, ignore_index=True
    )
    return grouped


def _add_lag_windows(df: pd.DataFrame) -> pd.DataFrame:
    """Steps 3.2-3.3 / 3.6-3.7: Add previous/next device info via shift().

    Adds: first_device_rank, last_device_rank, previous/next device dates
    and names.
    """
    df = df.sort_values(
        ["main_number_sk", "device_first_use_date"], ignore_index=True
    ).copy()

    g = df.groupby("main_number_sk", sort=False)

    # Ranks
    df["first_device_rank"] = g.cumcount() + 1
    df["last_device_rank"] = g.cumcount(ascending=False) + 1

    # Previous (lag) - shift forward
    df["previous_device_first_use_date"] = g["device_first_use_date"].shift(1)
    df["previous_device_release_date"] = g["device_release_date"].shift(1)
    df["pre_device"] = g["device_marketing_name"].shift(1)
    df["pre_producer"] = g["device_producername"].shift(1)

    # Next (lead) - shift backward
    df["next_device_first_use_date"] = g["device_first_use_date"].shift(-1)
    df["next_device"] = g["device_marketing_name"].shift(-1)
    df["next_producer"] = g["device_producername"].shift(-1)

    return df


def _remove_replacement_devices(df: pd.DataFrame, min_days: int) -> pd.DataFrame:
    """Step 3.4: Remove replacement/temporary devices.

    Keep a device if:
    - It is the first device for the subscriber, OR
    - It is the last (current) device for the subscriber, OR
    - It is different from the previous device AND was used for more than min_days
    """
    is_first = df["first_device_rank"] == 1
    is_last = df["last_device_rank"] == 1

    different_from_prev = (
        df["device_marketing_name"].str.upper() != df["pre_device"].str.upper()
    )
    days_used = (
        df["next_device_first_use_date"] - df["device_first_use_date"]
    ).dt.days
    used_long_enough = days_used > min_days

    keep = is_first | is_last | (different_from_prev & used_long_enough)

    # Drop lag columns before re-lagging in pass 2
    result = df.loc[keep].drop(
        columns=[
            "first_device_rank", "last_device_rank",
            "previous_device_first_use_date", "previous_device_release_date",
            "pre_device", "pre_producer",
            "next_device_first_use_date", "next_device", "next_producer",
        ],
    ).copy()

    return result.reset_index(drop=True)


def _remove_downgrades(df: pd.DataFrame) -> pd.DataFrame:
    """Step 3.5: Remove downgrade devices.

    For each subscriber, compute the cumulative max of device_release_date.
    Only keep devices whose release_date >= the max release date seen so far.
    This filters out cases where a subscriber switches to an older device.
    """
    df = df.sort_values(
        ["main_number_sk", "device_first_use_date"], ignore_index=True
    ).copy()

    df["max_release_to_date"] = df.groupby("main_number_sk")[
        "device_release_date"
    ].cummax()

    result = df[df["device_release_date"] >= df["max_release_to_date"]].copy()
    result.drop(columns=["max_release_to_date"], inplace=True)

    # Drop lag columns if they exist (from pass 1) before pass 2 re-lags
    lag_cols = [
        "first_device_rank", "last_device_rank",
        "previous_device_first_use_date", "previous_device_release_date",
        "pre_device", "pre_producer",
        "next_device_first_use_date", "next_device", "next_producer",
    ]
    existing_lag_cols = [c for c in lag_cols if c in result.columns]
    if existing_lag_cols:
        result.drop(columns=existing_lag_cols, inplace=True)

    return result.reset_index(drop=True)


def _compute_day_intervals(df: pd.DataFrame) -> pd.DataFrame:
    """Step 3.8: Compute day intervals between device transitions.

    Adds:
    - days_since_previous_device: days from previous device first use to this one
    - days_to_next_device: days from this device first use to next one
    - days_first_use_after_release: days from device release to first use
    """
    df = df.copy()

    # days_since_previous_device (null for first device)
    df["days_since_previous_device"] = None
    has_prev = df["first_device_rank"] > 1
    df.loc[has_prev, "days_since_previous_device"] = (
        df.loc[has_prev, "device_first_use_date"]
        - df.loc[has_prev, "previous_device_first_use_date"]
    ).dt.days

    # days_to_next_device (null for last/current device)
    df["days_to_next_device"] = None
    has_next = df["last_device_rank"] > 1
    df.loc[has_next, "days_to_next_device"] = (
        df.loc[has_next, "next_device_first_use_date"]
        - df.loc[has_next, "device_first_use_date"]
    ).dt.days

    # days_first_use_after_release (null for first device, matching POC)
    df["days_first_use_after_release"] = None
    df.loc[has_prev, "days_first_use_after_release"] = (
        df.loc[has_prev, "device_first_use_date"]
        - df.loc[has_prev, "device_release_date"]
    ).dt.days

    # Convert to float for downstream numeric operations
    for col in [
        "days_since_previous_device",
        "days_to_next_device",
        "days_first_use_after_release",
    ]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

"""Compute device change statistics at three levels of aggregation.

Replaces the three intermediate statistics tables from the POC SQL:
- main_stat_tmp     → compute_subscriber_stats()
- gen_stat_tmp      → compute_market_stats()
- device_name_stat_tmp → compute_device_model_stats()
"""

from __future__ import annotations

import logging

import pandas as pd

logger = logging.getLogger(__name__)


def compute_subscriber_stats(device_history: pd.DataFrame) -> pd.DataFrame:
    """Per-subscriber statistics: median days between device changes.

    Returns the device history enriched with med_days_since_previous_device
    (the subscriber's personal median change frequency).
    """
    df = device_history[device_history["device_marketing_name"].notna()].copy()

    medians = (
        df[df["days_since_previous_device"].notna()]
        .groupby("main_number_sk")["days_since_previous_device"]
        .median()
        .rename("med_days_since_previous_device")
    )
    df = df.merge(medians, on="main_number_sk", how="left")

    logger.info("Subscriber stats: %d rows, %d subscribers", len(df), medians.shape[0])
    return df


def compute_market_stats(device_history: pd.DataFrame) -> pd.DataFrame:
    """Market-level statistics per month across all subscribers.

    Returns DataFrame with monthly avg/median/stddev of change days.
    """
    df = device_history[device_history["days_since_previous_device"].notna()].copy()
    df["first_use_month"] = df["device_first_use_date"].dt.to_period("M").dt.to_timestamp()

    # Compute subscriber-level median first (matching POC's PERCENTILE_CONT window)
    sub_medians = (
        df.groupby("main_number_sk")["days_since_previous_device"]
        .median()
        .rename("sub_med")
    )
    df = df.merge(sub_medians, on="main_number_sk", how="left")

    stats = (
        df.groupby("first_use_month")
        .agg(
            avg_gen_days_first_use_after_release=("days_first_use_after_release", "mean"),
            avg_gen_change_days=("days_since_previous_device", "mean"),
            med_gen_change_days=("sub_med", "mean"),
            stddev_gen_change_days=("days_since_previous_device", "std"),
        )
        .reset_index()
    )

    logger.info("Market stats: %d months", len(stats))
    return stats


def compute_device_model_stats(device_history: pd.DataFrame) -> pd.DataFrame:
    """Per-device-model statistics per month.

    Returns DataFrame with avg/median/stddev of days_to_next_device
    for each device model and month.

    Note: The POC had a bug where med_dev_change_days was computed as AVG
    instead of actual median. This implementation uses the correct median.
    """
    df = device_history[device_history["days_to_next_device"].notna()].copy()
    df["first_use_month"] = df["device_first_use_date"].dt.to_period("M").dt.to_timestamp()

    stats = (
        df.groupby(["first_use_month", "device_marketing_name"])
        .agg(
            avg_dev_days_first_use_after_release=("days_first_use_after_release", "mean"),
            avg_dev_change_days=("days_to_next_device", "mean"),
            med_dev_change_days=("days_to_next_device", "median"),
            stddev_dev_change_days=("days_to_next_device", "std"),
        )
        .reset_index()
    )

    logger.info("Device model stats: %d entries", len(stats))
    return stats

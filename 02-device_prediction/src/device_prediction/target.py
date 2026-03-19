"""Survival analysis target construction.

Replaces the binary device_target from the POC with a survival target:
(duration_months, event) where duration is time-to-device-change and
event indicates whether the change was actually observed (1) or censored (0).
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from device_prediction.config import Settings

logger = logging.getLogger(__name__)


def construct_survival_target(
    feature_matrix: pd.DataFrame,
    subscriber_stats: pd.DataFrame,
    cfg: Settings,
) -> pd.DataFrame:
    """Add survival target columns to the feature matrix.

    For each observation (subscriber S at month T with device D):
    1. Find the next device change after T from subscriber_stats
    2. Compute duration_months from T to next change (or end of data)
    3. Set event=1 if change observed, event=0 if censored

    Censoring rules:
    - Right-censored if no device change observed within max_horizon_months
    - Right-censored at end of available data
    """
    logger.info("Constructing survival target for %d observations", len(feature_matrix))

    df = feature_matrix.copy()
    max_horizon = cfg.target.max_horizon_months

    # Build a lookup of all device changes per subscriber
    # (each row in subscriber_stats where first_device_rank > 1 represents a change)
    changes = subscriber_stats[
        subscriber_stats["device_first_use_date"].notna()
    ][["main_number_sk", "device_marketing_name", "device_first_use_date"]].copy()

    changes["change_date"] = pd.to_datetime(changes["device_first_use_date"])
    changes.sort_values(["main_number_sk", "change_date"], inplace=True)

    # For each subscriber, find the last observed date (end of data)
    last_observed = (
        changes.groupby("main_number_sk")["change_date"]
        .max()
        .rename("last_observed_date")
    )

    # Also consider the feature matrix periods for last observed
    df["_period"] = pd.to_datetime(df["period_month_date"])
    period_max = df.groupby("main_number_sk")["_period"].max().rename("last_period_date")
    end_dates = pd.concat([last_observed, period_max], axis=1)
    end_dates["data_end_date"] = end_dates.max(axis=1)

    # For each observation, find the next device change AFTER the observation period
    durations = []
    events = []

    # Index changes for fast lookup
    changes_by_sub = {
        sub: grp.sort_values("change_date")
        for sub, grp in changes.groupby("main_number_sk")
    }

    for _, row in df.iterrows():
        sub_id = row["main_number_sk"]
        obs_date = row["_period"]
        current_device = row.get("device_marketing_name", row.get("current_device", ""))

        sub_changes = changes_by_sub.get(sub_id)

        if sub_changes is not None:
            # Find next change: a different device with first_use_date > obs_date
            future_changes = sub_changes[
                (sub_changes["change_date"] > obs_date)
                & (sub_changes["device_marketing_name"] != current_device)
            ]

            if not future_changes.empty:
                next_change_date = future_changes.iloc[0]["change_date"]
                months = _months_between(obs_date, next_change_date)
                if months <= max_horizon:
                    durations.append(months)
                    events.append(1)
                    continue

        # Censored: no change observed within horizon
        data_end = end_dates.loc[sub_id, "data_end_date"] if sub_id in end_dates.index else obs_date
        months = min(_months_between(obs_date, data_end), max_horizon)
        months = max(months, 0.5)  # minimum half a month
        durations.append(months)
        events.append(0)

    df["duration_months"] = durations
    df["event"] = events
    df.drop(columns=["_period"], inplace=True)

    diagnostics = validate_survival_target(df)
    logger.info(
        "Survival target: %d events (%.1f%%), %d censored, median duration %.1f months",
        diagnostics["events"],
        diagnostics["event_rate"] * 100,
        diagnostics["censored"],
        diagnostics["median_duration_events"],
    )

    return df


def construct_survival_target_vectorized(
    feature_matrix: pd.DataFrame,
    subscriber_stats: pd.DataFrame,
    cfg: Settings,
) -> pd.DataFrame:
    """Vectorized version of survival target construction for large datasets.

    Uses merge_asof instead of row-by-row iteration.
    """
    logger.info("Constructing survival target (vectorized) for %d observations", len(feature_matrix))

    df = feature_matrix.copy()
    max_horizon = cfg.target.max_horizon_months

    df["_period"] = pd.to_datetime(df["period_month_date"])

    # Get all device change events (transitions to a new device)
    changes = subscriber_stats[
        subscriber_stats["device_first_use_date"].notna()
    ][["main_number_sk", "device_marketing_name", "device_first_use_date"]].copy()
    changes["change_date"] = pd.to_datetime(changes["device_first_use_date"])
    changes.sort_values(["main_number_sk", "change_date"], inplace=True)

    # End of data per subscriber
    data_end = changes.groupby("main_number_sk")["change_date"].max().rename("data_end_date")
    period_end = df.groupby("main_number_sk")["_period"].max().rename("last_period")
    end_dates = pd.DataFrame({"data_end_date": data_end, "last_period": period_end}).max(axis=1).rename("data_end_date")

    # For each observation, find the first change AFTER the observation
    # Use merge_asof per subscriber group
    df = df.sort_values(["main_number_sk", "_period"]).reset_index(drop=True)
    changes_sorted = changes.sort_values(["main_number_sk", "change_date"]).reset_index(drop=True)

    # merge_asof: for each observation, find the nearest future change
    merged = pd.merge_asof(
        df[["main_number_sk", "_period"]].sort_values("_period"),
        changes_sorted[["main_number_sk", "change_date"]].sort_values("change_date"),
        by="main_number_sk",
        left_on="_period",
        right_on="change_date",
        direction="forward",
        allow_exact_matches=False,
    )

    df["next_change_date"] = merged["change_date"].values

    # Compute duration and event
    df = df.merge(end_dates.reset_index(), on="main_number_sk", how="left")

    has_change = df["next_change_date"].notna()
    change_months = _months_between_series(df["_period"], df["next_change_date"])
    censor_months = _months_between_series(df["_period"], df["data_end_date"])

    df["duration_months"] = np.where(
        has_change & (change_months <= max_horizon),
        change_months,
        np.minimum(censor_months, max_horizon),
    )
    df["event"] = np.where(
        has_change & (change_months <= max_horizon), 1, 0
    ).astype(int)

    # Enforce minimum duration
    df["duration_months"] = df["duration_months"].clip(lower=0.5)

    df.drop(columns=["_period", "next_change_date", "data_end_date"], inplace=True, errors="ignore")

    diagnostics = validate_survival_target(df)
    logger.info(
        "Survival target: %d events (%.1f%%), %d censored, median duration %.1f months",
        diagnostics["events"],
        diagnostics["event_rate"] * 100,
        diagnostics["censored"],
        diagnostics["median_duration_events"],
    )

    return df


def validate_survival_target(df: pd.DataFrame) -> dict:
    """Compute diagnostic statistics about the survival target."""
    total = len(df)
    n_events = int(df["event"].sum())
    n_censored = total - n_events

    events_df = df[df["event"] == 1]
    censored_df = df[df["event"] == 0]

    return {
        "total_observations": total,
        "events": n_events,
        "censored": n_censored,
        "event_rate": n_events / max(total, 1),
        "median_duration_events": float(events_df["duration_months"].median()) if len(events_df) > 0 else 0.0,
        "median_duration_censored": float(censored_df["duration_months"].median()) if len(censored_df) > 0 else 0.0,
        "mean_duration": float(df["duration_months"].mean()),
    }


def _months_between(d1: pd.Timestamp, d2: pd.Timestamp) -> float:
    """Approximate months between two dates."""
    return max((d2 - d1).days / 30.44, 0)


def _months_between_series(s1: pd.Series, s2: pd.Series) -> pd.Series:
    """Approximate months between two date series."""
    return ((s2 - s1).dt.days / 30.44).clip(lower=0)

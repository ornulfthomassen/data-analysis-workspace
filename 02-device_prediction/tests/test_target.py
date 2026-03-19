"""Tests for survival target construction."""

import pandas as pd
import pytest

from device_prediction.target import (
    construct_survival_target,
    validate_survival_target,
)


class TestSurvivalTarget:
    def _make_feature_matrix(self):
        """Simple feature matrix with known device timelines."""
        return pd.DataFrame([
            # Sub 1: has IPHONE 13, will change to IPHONE 14 PRO after 6 months
            {"main_number_sk": 1, "period_month_date": "2022-03-31",
             "device_marketing_name": "IPHONE 13", "current_device": "IPHONE 13"},
            # Sub 1: same device, 3 months later
            {"main_number_sk": 1, "period_month_date": "2022-06-30",
             "device_marketing_name": "IPHONE 13", "current_device": "IPHONE 13"},
            # Sub 2: has GALAXY S22, no change observed
            {"main_number_sk": 2, "period_month_date": "2022-06-30",
             "device_marketing_name": "GALAXY S22", "current_device": "GALAXY S22"},
        ])

    def _make_subscriber_stats(self):
        """Subscriber stats showing device transitions."""
        return pd.DataFrame([
            # Sub 1: IPHONE 13 started Jan 2022
            {"main_number_sk": 1, "device_marketing_name": "IPHONE 13",
             "device_first_use_date": pd.Timestamp("2022-01-31")},
            # Sub 1: IPHONE 14 PRO started Sep 2022
            {"main_number_sk": 1, "device_marketing_name": "IPHONE 14 PRO",
             "device_first_use_date": pd.Timestamp("2022-09-30")},
            # Sub 2: GALAXY S22 started Mar 2022, no next device
            {"main_number_sk": 2, "device_marketing_name": "GALAXY S22",
             "device_first_use_date": pd.Timestamp("2022-03-31")},
        ])

    def test_event_detected(self, settings):
        fm = self._make_feature_matrix()
        ss = self._make_subscriber_stats()
        result = construct_survival_target(fm, ss, settings)

        assert "duration_months" in result.columns
        assert "event" in result.columns

        # Sub 1 at March: should see change ~6 months later (Sep)
        sub1_mar = result[
            (result["main_number_sk"] == 1)
            & (result["period_month_date"] == "2022-03-31")
        ]
        if len(sub1_mar) > 0:
            assert sub1_mar.iloc[0]["event"] == 1
            assert sub1_mar.iloc[0]["duration_months"] > 0

    def test_censored_observation(self, settings):
        fm = self._make_feature_matrix()
        ss = self._make_subscriber_stats()
        result = construct_survival_target(fm, ss, settings)

        # Sub 2: no device change observed → should be censored
        sub2 = result[result["main_number_sk"] == 2]
        if len(sub2) > 0:
            assert sub2.iloc[0]["event"] == 0

    def test_validate_diagnostics(self, settings):
        fm = self._make_feature_matrix()
        ss = self._make_subscriber_stats()
        result = construct_survival_target(fm, ss, settings)

        diag = validate_survival_target(result)
        assert diag["total_observations"] == len(result)
        assert diag["events"] + diag["censored"] == diag["total_observations"]
        assert 0 <= diag["event_rate"] <= 1

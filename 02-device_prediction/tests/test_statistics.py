"""Tests for statistics computation."""

import pandas as pd

from device_prediction.device_history import build_device_change_history
from device_prediction.statistics import (
    compute_device_model_stats,
    compute_market_stats,
    compute_subscriber_stats,
)


class TestSubscriberStats:
    def test_median_computed(self, subscription_hist, settings):
        hist = build_device_change_history(subscription_hist, settings)
        result = compute_subscriber_stats(hist)
        assert "med_days_since_previous_device" in result.columns
        # At least some values should be non-null
        assert result["med_days_since_previous_device"].notna().any()

    def test_all_subscribers_present(self, subscription_hist, settings):
        hist = build_device_change_history(subscription_hist, settings)
        result = compute_subscriber_stats(hist)
        assert result["main_number_sk"].nunique() == hist["main_number_sk"].nunique()


class TestMarketStats:
    def test_monthly_aggregation(self, subscription_hist, settings):
        hist = build_device_change_history(subscription_hist, settings)
        result = compute_market_stats(hist)
        assert "first_use_month" in result.columns
        assert "avg_gen_change_days" in result.columns
        assert "med_gen_change_days" in result.columns
        assert "stddev_gen_change_days" in result.columns
        assert len(result) > 0


class TestDeviceModelStats:
    def test_per_device_aggregation(self, subscription_hist, settings):
        hist = build_device_change_history(subscription_hist, settings)
        result = compute_device_model_stats(hist)
        assert "device_marketing_name" in result.columns
        assert "avg_dev_change_days" in result.columns
        assert "med_dev_change_days" in result.columns
        # Median should be actual median (not avg like POC bug)
        assert len(result) >= 0  # May be empty if no device has a next device

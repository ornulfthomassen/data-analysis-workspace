"""Tests for feature matrix assembly."""

from device_prediction.device_history import build_device_change_history
from device_prediction.features import build_feature_matrix
from device_prediction.statistics import (
    compute_device_model_stats,
    compute_market_stats,
    compute_subscriber_stats,
)


class TestFeatureMatrix:
    def _build_inputs(self, subscription_hist, settings):
        hist = build_device_change_history(subscription_hist, settings)
        sub_stats = compute_subscriber_stats(hist)
        mkt_stats = compute_market_stats(hist)
        dev_stats = compute_device_model_stats(hist)
        return sub_stats, mkt_stats, dev_stats

    def test_basic_assembly(self, subscription_hist, device_features, settings):
        sub_stats, mkt_stats, dev_stats = self._build_inputs(subscription_hist, settings)
        result = build_feature_matrix(
            subscription_hist, sub_stats, mkt_stats, dev_stats,
            device_features, settings, mode="train",
        )
        assert len(result) > 0
        # Should have seasonal features
        assert "days_until_christmas" in result.columns
        assert "days_until_summer" in result.columns
        assert "current_month_nr" in result.columns

    def test_device_features_joined(self, subscription_hist, device_features, settings):
        sub_stats, mkt_stats, dev_stats = self._build_inputs(subscription_hist, settings)
        result = build_feature_matrix(
            subscription_hist, sub_stats, mkt_stats, dev_stats,
            device_features, settings, mode="train",
        )
        # Device spec columns should be present
        assert "ram_gb" in result.columns
        assert "storage_base_gb" in result.columns
        assert "launch_price_nok" in result.columns

    def test_computed_features_present(self, subscription_hist, device_features, settings):
        sub_stats, mkt_stats, dev_stats = self._build_inputs(subscription_hist, settings)
        result = build_feature_matrix(
            subscription_hist, sub_stats, mkt_stats, dev_stats,
            device_features, settings, mode="train",
        )
        assert "current_device_release_days" in result.columns

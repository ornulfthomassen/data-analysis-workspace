"""Shared test fixtures with synthetic DataFrames."""

import pandas as pd
import pytest


@pytest.fixture
def subscription_hist():
    """Synthetic subscription history for 2 subscribers."""
    records = []
    # Subscriber 1: had 3 devices over time
    # Device A: Jan 2022 - Jun 2022 (released Dec 2021)
    for month in pd.date_range("2022-01-31", "2022-06-30", freq="ME"):
        records.append({
            "main_number_sk": 1001,
            "period_month_date": month,
            "device_marketing_name": "IPHONE 13",
            "device_producername": "APPLE",
            "device_release_date": pd.Timestamp("2021-09-30"),
            "device_category": "SMARTPHONE 5G",
            "device_group": "Mobile phone",
            "net_revenue": 350.0,
            "net_fee": 299.0,
            "net_use": 51.0,
            "mb_last1": 5000.0,
            "mb_last2": 4800.0,
            "mb_last3": 4500.0,
            "kr_mb_last1": 0.0,
            "kr_mb_last2": 0.0,
            "kr_mb_last3": 0.0,
            "no_days_mno_start": 1500.0,
            "no_days_prod_start": 400.0,
            "no_days_subs_start": 1200.0,
            "net_other_fee": 0.0,
            "net_discount_amount_use": -50.0,
            "net_amount_use_cpa_3mo": 150.0,
            "net_amount_use_roam_3mo": 10.0,
            "net_per_fee_bind_3mo": 897.0,
            "no_mms_dom_last1": 2.0,
            "net_disc_amt_use_roam_3mo": 0.0,
            "net_revenue_adj_3mo": 1050.0,
        })
    # Device B: Jul 2022 - Dec 2022 (released Jun 2022)
    for month in pd.date_range("2022-07-31", "2022-12-31", freq="ME"):
        rec = records[-1].copy()
        rec["period_month_date"] = month
        rec["device_marketing_name"] = "IPHONE 14 PRO"
        rec["device_release_date"] = pd.Timestamp("2022-09-30")
        records.append(rec)
    # Device C: Jan 2023 - Jun 2023 (released Sep 2023 - intentionally future for test)
    for month in pd.date_range("2023-01-31", "2023-06-30", freq="ME"):
        rec = records[-1].copy()
        rec["period_month_date"] = month
        rec["device_marketing_name"] = "IPHONE 15"
        rec["device_release_date"] = pd.Timestamp("2023-09-30")
        records.append(rec)

    # Subscriber 2: had 2 devices
    for month in pd.date_range("2022-03-31", "2022-12-31", freq="ME"):
        records.append({
            "main_number_sk": 2002,
            "period_month_date": month,
            "device_marketing_name": "GALAXY S22",
            "device_producername": "SAMSUNG",
            "device_release_date": pd.Timestamp("2022-02-28"),
            "device_category": "SMARTPHONE 5G",
            "device_group": "Mobile phone",
            "net_revenue": 280.0,
            "net_fee": 249.0,
            "net_use": 31.0,
            "mb_last1": 3000.0,
            "mb_last2": 3200.0,
            "mb_last3": 2800.0,
            "kr_mb_last1": 0.0,
            "kr_mb_last2": 0.0,
            "kr_mb_last3": 0.0,
            "no_days_mno_start": 800.0,
            "no_days_prod_start": 200.0,
            "no_days_subs_start": 600.0,
            "net_other_fee": 0.0,
            "net_discount_amount_use": -30.0,
            "net_amount_use_cpa_3mo": 90.0,
            "net_amount_use_roam_3mo": 5.0,
            "net_per_fee_bind_3mo": 747.0,
            "no_mms_dom_last1": 0.0,
            "net_disc_amt_use_roam_3mo": 0.0,
            "net_revenue_adj_3mo": 840.0,
        })
    for month in pd.date_range("2023-01-31", "2023-06-30", freq="ME"):
        rec = records[-1].copy()
        rec["period_month_date"] = month
        rec["device_marketing_name"] = "GALAXY S23"
        rec["device_release_date"] = pd.Timestamp("2023-02-28")
        records.append(rec)

    return pd.DataFrame(records)


@pytest.fixture
def device_features():
    """Synthetic device features table."""
    return pd.DataFrame([
        {
            "user_input": "APPLE IPHONE 13",
            "device_name": "IPHONE 13",
            "manufacturer": "APPLE",
            "release_year": 2021,
            "ram_gb": 4.0,
            "storage_base_gb": 128.0,
            "display_type": "OLED",
            "display_size_inches": 6.1,
            "camera_rear_mp": 12.0,
            "camera_front_mp": 12.0,
            "launch_price_nok": 10990.0,
            "device_series_annual": "Flagship",
            "device_series_annual_no": 5,
            "generation": "13",
            "context_summary": "Standard flagship",
        },
        {
            "user_input": "APPLE IPHONE 14 PRO",
            "device_name": "IPHONE 14 PRO",
            "manufacturer": "APPLE",
            "release_year": 2022,
            "ram_gb": 6.0,
            "storage_base_gb": 128.0,
            "display_type": "OLED",
            "display_size_inches": 6.1,
            "camera_rear_mp": 48.0,
            "camera_front_mp": 12.0,
            "launch_price_nok": 13990.0,
            "device_series_annual": "Premium Flagship",
            "device_series_annual_no": 6,
            "generation": "14",
            "context_summary": "Premium flagship with Dynamic Island",
        },
        {
            "user_input": "APPLE IPHONE 15",
            "device_name": "IPHONE 15",
            "manufacturer": "APPLE",
            "release_year": 2023,
            "ram_gb": 6.0,
            "storage_base_gb": 128.0,
            "display_type": "OLED",
            "display_size_inches": 6.1,
            "camera_rear_mp": 48.0,
            "camera_front_mp": 12.0,
            "launch_price_nok": 11990.0,
            "device_series_annual": "Flagship",
            "device_series_annual_no": 5,
            "generation": "15",
            "context_summary": "Standard flagship with USB-C",
        },
        {
            "user_input": "SAMSUNG GALAXY S22",
            "device_name": "GALAXY S22",
            "manufacturer": "SAMSUNG",
            "release_year": 2022,
            "ram_gb": 8.0,
            "storage_base_gb": 128.0,
            "display_type": "AMOLED",
            "display_size_inches": 6.1,
            "camera_rear_mp": 50.0,
            "camera_front_mp": 10.0,
            "launch_price_nok": 9990.0,
            "device_series_annual": "Flagship",
            "device_series_annual_no": 5,
            "generation": "22",
            "context_summary": "Samsung flagship",
        },
        {
            "user_input": "SAMSUNG GALAXY S23",
            "device_name": "GALAXY S23",
            "manufacturer": "SAMSUNG",
            "release_year": 2023,
            "ram_gb": 8.0,
            "storage_base_gb": 128.0,
            "display_type": "AMOLED",
            "display_size_inches": 6.1,
            "camera_rear_mp": 50.0,
            "camera_front_mp": 12.0,
            "launch_price_nok": 10490.0,
            "device_series_annual": "Flagship",
            "device_series_annual_no": 5,
            "generation": "23",
            "context_summary": "Samsung flagship with Snapdragon",
        },
    ])


@pytest.fixture
def settings():
    """Test settings with defaults."""
    from device_prediction.config import Settings
    return Settings()

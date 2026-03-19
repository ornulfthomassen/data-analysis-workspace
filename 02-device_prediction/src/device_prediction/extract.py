"""Extract subscription history from BigQuery, parameterized for train/score mode.

The SQL runs server-side in BigQuery (source tables are too large for local pandas).
Only the filtered/joined result is pulled into Python.
"""

from __future__ import annotations

import logging
from typing import Literal

import pandas as pd

from device_prediction import bq_client
from device_prediction.config import Settings

logger = logging.getLogger(__name__)


def extract_subscription_history(
    cfg: Settings,
    mode: Literal["train", "score"],
) -> pd.DataFrame:
    """Extract subscription history from BigQuery.

    Train mode: random sample of active subscribers, N years of history.
    Score mode: all active subscribers, current month only.
    """
    query = _build_extraction_query(cfg, mode)
    logger.info("Extracting subscription history (mode=%s)", mode)
    df = bq_client.read_query(query, cfg.bigquery.project_id)
    logger.info("Extracted %d rows in %s mode", len(df), mode)
    return df


def _build_extraction_query(cfg: Settings, mode: Literal["train", "score"]) -> str:
    """Build parameterized SQL for subscription history extraction.

    Shared logic (both modes):
    - JOIN subscription_hist with subscription_master_history for main_number_sk
    - Derive device_release_date as MIN(period_month_date) per device model
    - Filter device_type to configured device types
    - UPPER normalization on device names

    Train-specific:
    - Sample active subscribers at configured rate
    - History window: N years back to M months before current date
    - No customer_sk_user

    Score-specific:
    - All active subscribers (no sampling)
    - Current month only
    - Include customer_sk_user
    """
    bq = cfg.bigquery
    ext = cfg.extraction

    device_type_list = ", ".join(f"'{dt}'" for dt in ext.device_types)

    # Score mode includes customer_sk_user; train does not
    customer_sk_col = "MAX(s.customer_sk_user) AS customer_sk_user," if mode == "score" else ""

    # Active subscribers filter
    if mode == "train":
        active_date_expr = (
            "DATE_SUB(DATE_ADD(DATE_TRUNC(CURRENT_DATE(), MONTH), "
            "INTERVAL 1 MONTH), INTERVAL 1 DAY)"
        )
        sample_filter = f"AND RAND() < {ext.train_sample_rate}"
    else:
        active_date_expr = (
            "DATE_SUB(DATE_ADD(DATE_TRUNC(CURRENT_DATE(), MONTH), "
            "INTERVAL 0 MONTH), INTERVAL 1 DAY)"
        )
        sample_filter = ""

    # History window filter
    if mode == "train":
        history_filter = (
            f"AND s.period_month_date BETWEEN "
            f"DATE_ADD(CURRENT_DATE(), INTERVAL -{ext.train_history_years} YEAR) "
            f"AND DATE_ADD(CURRENT_DATE(), INTERVAL -{ext.train_buffer_months} MONTH)"
        )
    else:
        history_filter = ""

    query = f"""
    WITH
    release_dates AS (
        SELECT
            UPPER(r.device_marketing_name) AS device_marketing_name,
            UPPER(r.device_producername) AS device_producername,
            MIN(r.period_month_date) AS device_release_date
        FROM `{bq.subscription_hist_table}` r
        WHERE r.period_month_date IS NOT NULL
            AND r.device_type IN ({device_type_list})
        GROUP BY ALL
    ),
    hist AS (
        SELECT
            m.main_number_sk,
            {customer_sk_col}
            s.period_month_date,
            UPPER(s.device_marketing_name) AS device_marketing_name,
            UPPER(s.device_producername) AS device_producername,
            rd.device_release_date,
            UPPER(s.device_category) AS device_category,
            CASE
                WHEN s.device_type IN ({device_type_list})
                THEN 'Mobile phone'
                ELSE 'Other device'
            END AS device_group,
            s.net_other_fee,
            s.no_days_mno_start,
            s.no_days_prod_start,
            s.net_discount_amount_use,
            s.net_amount_use_cpa_3mo,
            s.kr_mb_last3,
            s.net_revenue,
            s.net_amount_use_roam_3mo,
            s.net_per_fee_bind_3mo,
            s.no_mms_dom_last1,
            s.kr_mb_last1,
            s.net_use,
            s.mb_last3,
            s.net_disc_amt_use_roam_3mo,
            s.mb_last1,
            s.kr_mb_last2,
            s.net_fee,
            s.no_days_subs_start,
            s.mb_last2,
            s.net_revenue_adj_3mo
        FROM `{bq.subscription_hist_table}` s
        LEFT JOIN `{bq.subscription_master_table}` m
            ON CAST(s.subscription_id AS NUMERIC) = m.subscription_id
        LEFT JOIN release_dates rd
            ON rd.device_marketing_name = UPPER(s.device_marketing_name)
            AND rd.device_producername = UPPER(s.device_producername)
        WHERE s.period_month_date IS NOT NULL
            AND s.device_type IN ({device_type_list})
            {history_filter}
        GROUP BY ALL
    ),
    active_subs AS (
        SELECT m.main_number_sk
        FROM `{bq.subscription_hist_table}` s
        LEFT JOIN `{bq.subscription_master_table}` m
            ON CAST(s.subscription_id AS NUMERIC) = m.subscription_id
        WHERE s.period_month_date = {active_date_expr}
            AND s.device_type IN ({device_type_list})
            {sample_filter}
    )
    SELECT h.*
    FROM hist h
    JOIN active_subs a ON h.main_number_sk = a.main_number_sk
    """
    return query

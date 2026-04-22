# GCP_STOCK_MOBILE_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates mobile subscription stock and balance data on a weekly basis. It combines historical weekly data with current daily data for the ongoing week, calculating total discounts, closing balance (UB_WEEK), opening balance (IB_WEEK), and net change (UB_WEEK - IB_WEEK). The data is segmented by various product profit categories (Tale), customer lifecycle segments for the owner, owner and user age groups, family bonus status, and discount product key. The view provides data for the last 24 months and is primarily intended for transfer to Google Cloud Platform (GCP).

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_WEEK_DIM_V]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_WEEK_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]


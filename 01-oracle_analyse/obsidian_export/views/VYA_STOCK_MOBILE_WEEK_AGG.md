# VYA_STOCK_MOBILE_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates weekly mobile subscription balance (stock) data. It calculates the closing balance (UB_WEEK), opening balance (IB_WEEK), and net change (NETTO) for each week. The data is enriched with dimensions such as period date and key, product key, 'Tale' profit categories, owner's customer lifecycle segment, owner and user age groups, family bonus flag, and discount details. The aggregation combines historical weekly data with recent daily data to provide a comprehensive weekly view, focusing on the last 24 months of activity.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_WEEK_DIM_V]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_WEEK_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_PROFIT_CAT_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]


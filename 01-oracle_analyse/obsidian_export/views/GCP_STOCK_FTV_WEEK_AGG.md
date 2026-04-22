# GCP_STOCK_FTV_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates weekly stock/balance data, including product details, customer types, lifecycle segments, age groups, and activation status. It calculates a total balance, an 'unbilled/initial' balance (UB_WEEK), a 'billed/invoiced' balance (IB_WEEK), and a 'net' balance (NETTO) at a weekly granularity. The view is specifically designed to prepare and lift this data through Denodo to Google Cloud Platform (GCP), pulling data for approximately the last two years.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_WEEK_DIM_V]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_WEEK_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG]]


# VYA_STOCK_FTV_WEEK_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates weekly stock-related financial transaction values (BALANCE, UB_WEEK, IB_WEEK, NETTO) across various dimensions for the last 24 months. It combines historical data from both weekly and daily stock aggregation tables, enriching it with descriptive information from dimension tables such as week details, customer lifecycle segments, and age groups. The 'NETTO' column specifically calculates the net change in balance (UB_WEEK - IB_WEEK) for each aggregated week. The aggregation provides a comprehensive weekly overview segmented by product, customer types (owner, payer, user), age groups, and customer lifecycle.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_WEEK_DIM_V]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_WEEK_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG]]


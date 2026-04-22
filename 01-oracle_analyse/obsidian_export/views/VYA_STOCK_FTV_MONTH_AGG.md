# VYA_STOCK_FTV_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a monthly aggregated view of Fiber-to-the-home (FTV) stock or subscription counts. It calculates the beginning-of-month balance (IB_MONTH), end-of-month balance (UB_MONTH), and the net monthly change (NETTO = UB_MONTH - IB_MONTH). This view combines historical monthly aggregated data with current month's daily aggregated data to provide up-to-date figures, categorized by various dimensions such as product keys, customer types, age groups, lifecycle segments, and dual-play indicators. The data is filtered to include the last 24 months.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_MONTH_AGG]]
- ← [[CRM_ANALYSE.ADM_CLM_LIVSFASE_DIM]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG]]


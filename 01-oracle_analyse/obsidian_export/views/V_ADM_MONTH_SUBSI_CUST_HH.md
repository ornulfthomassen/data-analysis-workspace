# V_ADM_MONTH_SUBSI_CUST_HH

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates monthly historical data for subscriptions, customers (both owner and last user), and their associated household information. It generates unique monthly and next-monthly identifiers for subscriptions, main IDs, customers, and households, based on historical snapshots. The view filters out specific test or known customer records and focuses on past monthly periods for analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]


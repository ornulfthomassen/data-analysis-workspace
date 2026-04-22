# GCP_TMP_SUBSCRIPTION_GROSS_FEE_GROSS_USE

**Schema:** `CCM` | **Type:** `View`

## Description
This view retrieves and consolidates aggregated gross fee and gross use amounts for subscriptions, identified by a period month and subscription ID. It combines data from a subscription aggregation table with a subscription history table, rounding the financial/usage metrics to two decimal places.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]


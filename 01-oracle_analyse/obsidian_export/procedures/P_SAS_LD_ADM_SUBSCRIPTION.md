# P_SAS_LD_ADM_SUBSCRIPTION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure loads historical monthly subscription data from a series of source tables (e.g., CLM_ADM.ADM_SUBSCRIPTION_YYYYMM) into a single target staging table (CLM_ADM.TMP_CHURN_ADM_SUBSCRIPTION). It iterates through the last 26 months (current month and 25 preceding months). For the oldest month (25 months ago), it truncates the target table and inserts the data. For all subsequent months (from 24 months ago up to the current month), it appends data to the target table, effectively consolidating historical subscription records.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_YYYYMM]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CHURN_ADM_SUBSCRIPTION]]


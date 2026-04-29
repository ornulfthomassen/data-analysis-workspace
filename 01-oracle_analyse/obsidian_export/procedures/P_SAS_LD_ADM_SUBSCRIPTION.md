# P_SAS_LD_ADM_SUBSCRIPTION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Consolidates historical monthly subscription data into a single temporary staging table. It iterates through tables suffixed with `YYYYMM` for the past 26 months (from 25 months ago to the current month). The target temporary table is truncated once at the beginning of the process, then data from each historical source table is appended to it.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_<YYYYMM_SUFFIX>]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CHURN_ADM_SUBSCRIPTION]]


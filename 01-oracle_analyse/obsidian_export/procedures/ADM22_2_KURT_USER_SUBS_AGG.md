# ADM22_2_KURT_USER_SUBS_AGG

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates user subscription data for specified periods (defined by P_YYYYMM_FRA and P_YYYYMM_TIL parameters). It performs data availability and consistency checks across various source tables related to dates, household information, and subscription history. The aggregated results are intended to be stored in a permanent table named 'ADM_KURT_USER_SUBS_AGG'. Although the full DML (INSERT/MERGE) statement is not visible due to the script being cut off, the variable definitions and cursor logic strongly indicate an aggregation and storage process.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_AGG]]

## Target Tables (Outputs)
- → [[ADM_KURT_USER_SUBS_AGG]]


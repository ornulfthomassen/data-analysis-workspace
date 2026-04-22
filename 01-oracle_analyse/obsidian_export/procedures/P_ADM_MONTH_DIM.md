# P_ADM_MONTH_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_MONTH_DIM rebuilds the CLM_ADM.ADM_MONTH_DIM table. It first drops a potentially existing older version (ADM_MONTH_DIM_OLD), renames the current ADM_MONTH_DIM to ADM_MONTH_DIM_OLD, and then creates a new CLM_ADM.ADM_MONTH_DIM table. This new table functions as a month-based time dimension, containing attributes for the current month, the next month, and the previous six months, derived by joining the CLM_ADM.ADM_MONTH_DIM_V view with itself multiple times. After creation, it grants SELECT privileges on the new ADM_MONTH_DIM table to CRM_ANALYSE and CCM roles, and logs the load history.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MONTH_DIM]]


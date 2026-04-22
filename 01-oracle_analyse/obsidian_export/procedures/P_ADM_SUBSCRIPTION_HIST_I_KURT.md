# P_ADM_SUBSCRIPTION_HIST_I_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBSCRIPTION_HIST_I_KURT generates and maintains a historical subscription data table named ADM_SUBSCRIPTION_HIST_I_KURT for a specific month (V_YYYYMM). It performs several steps: First, it validates the availability and recency of data in multiple source tables. If data is missing or not up-to-date, it raises an error. If the target table ADM_SUBSCRIPTION_HIST_I_KURT already exists and an overwrite is required (either explicitly or due to outdated data), it renames the existing table to ADM_SUBSCRIPTION_HIST_I_KURT_O (acting as a backup) and updates its associated index. Subsequently, it creates two intermediate temporary tables, TMP1_SUBSCRIPTION_HIST_I_KURT and TMP2_SUBSCRIPTION_HIST_I_KURT, which are populated by joining and filtering data from various source systems. Finally, it creates the main target table ADM_SUBSCRIPTION_HIST_I_KURT, selecting processed data from the second temporary table. The procedure includes comprehensive error handling, logging, and performance optimization steps such as creating indexes and gathering statistics on all newly created tables.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CRM_ANALYSE.TDM_MOBIL_SUBSCR_HIST]]
- ← [[ADM_SUBSCRIPTION_HIST_KURT]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_HIST_I_KURT]]
- → [[ADM_SUBSCRIPTION_HIST_I_KURT_O]]
- → [[TMP1_SUBSCRIPTION_HIST_I_KURT]]
- → [[TMP2_SUBSCRIPTION_HIST_I_KURT]]


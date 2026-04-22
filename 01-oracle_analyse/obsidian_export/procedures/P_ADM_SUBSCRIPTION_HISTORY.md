# P_ADM_SUBSCRIPTION_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_SUBSCRIPTION_HISTORY` manages and populates monthly partitions of the `ADM_SUBSCRIPTION_HISTORY` table. It begins by validating the availability of source data for a given month (`P_YYYYMM`) across several `ADM_MONTH_DIM`, `ADM_SUBSCRIPTION_HIST_KURT`, `ADM_SUBSCRIPTION_MASTER_HIST`, and `ADM_CUSTOMER_MAPPING_HIST` tables. If validation passes, it checks for the existence of the target partition in `ADM_SUBSCRIPTION_HISTORY`, creating it if necessary or preventing overwrites of existing data. A temporary table named `TMP_SUBSCRIPTION_HISTORY` is then created and populated with transformed historical subscription data from `CLM_ADM.ADM_SUBSCRIPTION_HIST_KURT`, `CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST`, and `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT`. Finally, it performs an `EXCHANGE PARTITION` operation to efficiently load this data into the corresponding partition of `ADM_SUBSCRIPTION_HISTORY` and gathers table statistics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HIST_KURT]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_HISTORY]]
- → [[TMP_SUBSCRIPTION_HISTORY]]


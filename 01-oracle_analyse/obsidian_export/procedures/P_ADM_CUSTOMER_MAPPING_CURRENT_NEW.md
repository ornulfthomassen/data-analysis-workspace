# P_ADM_CUSTOMER_MAPPING_CURRENT_NEW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_CUSTOMER_MAPPING_CURRENT_new` is responsible for refreshing or rebuilding the primary customer mapping table `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW`. It first performs a data validation check on `CCDW.CUSTOMER_MAPPING`. If the validation passes, it backs up the existing `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW` table into `CLM_ADM.ADM_CUSTOMER_MAPPING_CURR_BCK_N` (dropping any pre-existing backup table first). Subsequently, it drops the `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW` table and recreates it by selecting and joining data from `CCDW.CUSTOMER_MAPPING_NEW`, `GALAXY.CUSTOMER_DIM`, and `CDC.MASTER_CUSTOMER`. Finally, it gathers statistics on the newly created table, creates unique indexes on it, and grants SELECT privileges to various roles.

## Data Sources (Inputs)
- ← [[CCDW.CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW]]
- ← [[CCDW.CUSTOMER_MAPPING_NEW]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CDC.MASTER_CUSTOMER]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURR_BCK_N]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW]]


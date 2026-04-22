# P_ADM_CUSTOMER_MAPPING_CURRENT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_CUSTOMER_MAPPING_CURRENT` procedure is designed to maintain and refresh a primary customer mapping table, `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT`. It first performs a data integrity check on its main source table (`CCDW.CUSTOMER_MAPPING`). If the check passes, it creates a backup of the existing `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT` table. Subsequently, it drops and recreates the `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT` table by performing a join operation across `CCDW.CUSTOMER_MAPPING`, `GALAXY.CUSTOMER_DIM`, and `CDC.MASTER_CUSTOMER` tables. Finally, it creates unique indexes on the newly built table and grants necessary SELECT privileges. The procedure includes extensive logging and error handling mechanisms.

## Data Sources (Inputs)
- ← [[CCDW.CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CDC.MASTER_CUSTOMER]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURR_BCK]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]


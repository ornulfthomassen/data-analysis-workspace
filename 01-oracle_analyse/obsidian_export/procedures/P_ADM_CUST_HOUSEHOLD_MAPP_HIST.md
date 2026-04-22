# P_ADM_CUST_HOUSEHOLD_MAPP_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Creates or updates a monthly partition in the `ADM_CUST_HOUSEHOLD_MAPP_HIST` table. It calculates customer household mappings for a given month by joining several source tables (`ADM_HOUSEHOLD_INFO_KURT_HIST`, `ADM_CUSTOMER_MAPPING_HIST`, `ADM_HOUSEHOLD_MAPPING_HIST`). The calculated data is first staged in a temporary table (`TMP_CUST_HOUSEHOLD_MAPP_HIST`) and then efficiently moved into the permanent partitioned table using an `ALTER TABLE ... EXCHANGE PARTITION` operation. The procedure also handles partition existence checks, creation, and statistics gathering, and includes logging and error handling.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_CUST_HOUSEHOLD_MAPP_HIST]]
- → [[TMP_CUST_HOUSEHOLD_MAPP_HIST]]


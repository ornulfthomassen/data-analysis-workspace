# P_ADM_CUSTOMER_MAPPING_CURRENT_NEW

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure recreates a customer mapping table (`ADM_CUSTOMER_MAPPING_CURRENT_NEW`) within the `CLM_ADM` schema. It first checks the status of the `CCDW.CUSTOMER_MAPPING` source table. If conditions are met, it backs up the existing `ADM_CUSTOMER_MAPPING_CURRENT_NEW` table into a new backup table (`ADM_CUSTOMER_MAPPING_CURR_BCK_N`), then drops the original `ADM_CUSTOMER_MAPPING_CURRENT_NEW` table and recreates it with fresh data aggregated from `CCDW.CUSTOMER_MAPPING_NEW`, `GALAXY.CUSTOMER_DIM`, and `CDC.MASTER_CUSTOMER`. Finally, it creates unique indexes on the new table and grants select privileges to various roles/users.

## Data Sources (Inputs)
- ← [[CCDW.CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW]]
- ← [[CCDW.CUSTOMER_MAPPING_NEW]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
| MAP_STATUS |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| CUSTOMER_KEY |
| COUNTERPART_KEY |
| DATE_OF_BIRTH |
| BIRTH_DATE_AGE |
| MAIN_ADDRESS_LOCATION_ID |
| POSTAL_ADDRESS_LOCATION_ID |
| MUNICIPAL_ID |
- ← [[CDC.MASTER_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| MASTER_ID |
| CUST_UNIT_NUMBER |
| INFO_IS_DELETED |
| CUST_UNIT_DATE |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURR_BCK_N]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT_NEW]]
| Column Name |
|---|
| KURT_ID |
| KURT_KEY |
| CUSTOMER_SK |
| CUSTOMER_KEY |
| MASTER_ID |
| CUST_UNIT_NUMBER |
| MAP_STATUS |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| COUNTERPART_KEY |
| DATE_OF_BIRTH |
| DATE_ID_OF_BIRTH |
| CURRENT_AGE |
| MAIN_ADDRESS_LOCATION_ID |
| POSTAL_ADDRESS_LOCATION_ID |
| MUNICIPAL_ID |


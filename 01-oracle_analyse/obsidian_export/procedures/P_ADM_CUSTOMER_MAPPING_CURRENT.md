# P_ADM_CUSTOMER_MAPPING_CURRENT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Rebuilds and maintains the CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT table. It first creates a backup of the existing table, then drops and recreates the current table with derived data by joining CCDW.CUSTOMER_MAPPING, GALAXY.CUSTOMER_DIM, and CDC.MASTER_CUSTOMER. The process includes source data validation, index creation, granting select privileges, and comprehensive error logging.

## Data Sources (Inputs)
- ← [[CCDW.CUSTOMER_MAPPING]]
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
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURR_BCK]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
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
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| LOAD_DATE |
| STATUS |
| MESSAGE |


# VYA_CCM_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and transforms customer and household-related data from multiple source views and tables (`CCM_CUSTOMER_V`, `ADM_CUSTOMER_MAPPING`, `ADM_HOUSEHOLD_MAPPING_V`, `ADM_AGE_GROUP_DIM`). It derives customer and household surrogate keys, handles anonymization for non-customer household SKs, and processes demographic information (age, gender) and communication consent flags (email, SMS). The view is intended for loading customer data into the Mjøsa analytical platform.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| CUSTOMER_STATUS_CD |
| CUSTOMER_TYPE_CD |
| AGE |
| GENDER |
| RES_BRSUND_DM |
| RES_BRSUND_DM_MAX_DTTM |
| RES_BRSUND_TM |
| RES_BRSUND_TM_MAX_DTTM |
| RES_TELENOR_DM |
| RES_TELENOR_DM_MAX_DTTM |
| RES_TELENOR_TM |
| RES_TELENOR_TM_MAX_DTTM |
| EMAIL_IND |
| EMAIL_MAX_RES_APP_DTTM |
| SMS_IND |
| SMS_MAX_RES_APP_DTTM |
| LOAD_DTTM |
| KURT_ID |
| HOUSEHOLD_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_MAPPING_V]]
| Column Name |
|---|
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ID |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_NAME_10C |
| AGE_GROUP_KEY |


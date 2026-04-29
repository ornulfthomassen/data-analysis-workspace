# P_RDM_CUSTOMER_MAPPING

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Orchestrates the monthly update, insertion, termination, and logical deletion (map-deletion) of customer mapping records in the `ADM_CUSTOMER_MAPPING` table. It processes customer and subscription history data from various source systems (like GALAXY, CLM_ADM, CCDW, KURT, ODS), identifies customer lifecycle changes (e.g., becoming a customer, an ex-customer, or a non-customer), and applies these changes to maintain a comprehensive customer mapping dataset. The procedure also manages control logs, creates temporary processing tables, generates a current valid mapping snapshot (`ADM_CUSTOMER_MAPPING_CURRENT`), and produces monthly historical snapshots (`ADM_CUSTOMER_MAPPING_<YYYYMM>`). It includes robust error handling and backup/restore mechanisms.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HIST_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| SUBS_NO_DAYS_ACTIVE |
| KURT_ID_USER |
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| ORDER_KURT_KEY_OWNER |
| PRODUCT_AGREEMENT_REG_DATE |
| PRODUCT_AGREEMENT_STATUS |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE_KEY |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| STATUS |
| ACTION_OWNER |
| ACTION_USER |
| ANTALL |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PREV1_PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_UD]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
| STATUS |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_PD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| STATUS |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| OWNER_FLG |
| OWNER_NUMBER_OF_TIMES |
| USER_FLG |
| USER_NUMBER_OF_TIMES |
| KURT_ID_DELETE_DATE |
| MAP_STATUS |
| STATUS_DATE |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
| KURT_ID_INSERT_DATE |
| KURT_ID_UPDATE_DATE |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| BUSINESS_AREA_ID |
| SOURCE_SYSTEM_ID |
| KURT_ID_OWNER |
| END_DATE |
| ORIGINAL_START_DATE |
| KURT_ID_USER |
- ← [[KURT.KURT]]
| Column Name |
|---|
| KID |
| KUNDE_TYPE |
| KUNDE_STATUS |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| ORGANIZATION_TYPE_ID |
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BACKUP]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_RAW]]
| Column Name |
|---|
| KURT_ID |
| KID |
| ACTION_OWNER |
| ACTION_USER |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| STATUS_DATE |
| OWNER_FLG |
| USER_FLG |
| OWNER_START_DATE |
| USER_START_DATE |
| KURT_ID_INSERT_DATE |
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| MAP_STATUS |
| STATUS_DATE |
| CUSTOMER_SK |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| OWNER_FLG |
| USER_FLG |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |
| KURT_ID_INSERT_DATE |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| STATUS_DATE |
| ACTION_OWNER |
| ACTION_USER |
| ANTALL |
| STATUS |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BACKUP_OK]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
| Column Name |
|---|
| KURT_ID |
| KURT_KEY |
| CUSTOMER_SK |
| CUSTOMER_KEY |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_<YYYYMM>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| KURT_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_UNIT_TYPE_ID |
| MAP_STATUS |
| STATUS_DATE |
| OWNER_FLG |
| USER_FLG |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
| OWNER_NUMBER_OF_TIMES |
| USER_NUMBER_OF_TIMES |
| KURT_ID_INSERT_DATE |
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |


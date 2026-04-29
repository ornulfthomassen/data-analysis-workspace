# P_RDM_CUSTOMER_MAPPING_UPDATE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_RDM_CUSTOMER_MAPPING_UPDATE` maintains and updates a central customer mapping table, `ADM_CUSTOMER_MAPPING`, based on daily subscription data. It processes data from various subscription sources (mobile, fixed-line, broadband) to identify new customer relationships, updates to existing customer details (e.g., status, type, flags, ownership/user counts), and inserts these changes into the main mapping table. The process involves creating a temporary raw staging table (`ADM_CUSTOMER_MAPPING_RAW`), utilizing a control table (`ADM_CUSTOMER_MAPPING_CTRL_UD`) to track and manage data actions, and maintaining backup versions of the main mapping table. Additionally, it generates 'current' and daily snapshot tables (`ADM_CUSTOMER_MAPPING_CURRENT` and `ADM_CUSTOMER_MAPPING_D<DATE>`) for reporting and historical purposes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
| OWNER_FLG |
| MAP_STATUS |
| OWNER_NUMBER_OF_TIMES |
| USER_FLG |
| USER_NUMBER_OF_TIMES |
| OWNER_START_DATE_ORIG |
| USER_START_DATE_ORIG |
| OWNER_START_DATE |
| USER_START_DATE |
| OWNER_END_DATE |
| USER_END_DATE |
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| LAST_OWNER |
| ORIGINAL_START_DATE |
| END_DATE |
| LAST_USER |
- ← [[CLM_ADM.ADM_FIX_BB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| LAST_OWNER |
| ORIGINAL_START_DATE |
| END_DATE |
| LAST_USER |
- ← [[CLM_ADM.ADM_FIX_TLF_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| LAST_USER |
| ORIGINAL_START_DATE |
| END_DATE |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| KURT_ID_OWNER |
| ORIGINAL_START_DATE |
| END_DATE |
| BUSINESS_AREA_ID |
| SOURCE_SYSTEM_ID |
| KURT_ID_USER |
- ← [[KURT.KURT]]
| Column Name |
|---|
| KID |
| KUNDE_TYPE |
| KUNDE_STATUS |
| ENH_TYPE |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_UD]]
| Column Name |
|---|
| STATUS |
| PERIOD_DATE_KEY |
| ACTION_OWNER |
| ACTION_USER |
| ANTALL |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_PD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| STATUS |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE |
| LAST_DATE |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
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
| KURT_ID_UPDATE_DATE |
| KURT_ID_DELETE_DATE |
| CUSTOMER_SK |
| KURT_ID |
| KURT_ID_INSERT_DATE |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_UD]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
| INSERT_DTTM |
| ACTION_OWNER |
| ACTION_USER |
| ANTALL |
| STATUS |
| UPDATE_DTTM |
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BCK_UD]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BCK_UD_OK]]
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
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
| Column Name |
|---|
| KURT_ID |
| KURT_KEY |
| CUSTOMER_SK |
| CUSTOMER_KEY |
- → [[ADM_CUSTOMER_MAPPING_D<DATE>]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
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


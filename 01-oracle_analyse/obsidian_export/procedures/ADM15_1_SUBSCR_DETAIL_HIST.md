# ADM15_1_SUBSCR_DETAIL_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure creates and populates a partitioned historical detail table, `CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST`, with aggregated and derived subscription data. It processes data month by month, validating source data availability, dynamically creating new partitions and indexes for each month if needed, and inserting detailed subscription information by joining multiple source tables. It also logs its operations and any errors encountered using an external logging procedure.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| PARENT |
| ID |
| DESCRIPTION |
| TYPE |
| SUBSTITUTION_PROD_ID1 |
| SOURCE_SYSTEM_KEY_PCAT |
| SOURCE_SYSTEM_KEY_PACMAN |
| VALUE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_KEY |
| PRODUCT_DESC |
| DRM_PRODUCT_DESC |
- ← [[PCAT.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| KURT_ID_OWNER |
| PRODUCT_OFFER_ID |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| END_DATE |
| INFO_CHG_DATE |
- ← [[CRM_ANALYSE.ADM_MAIN_NUMBER_BANKID]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| BANKID_USED_LAST1 |
| BANKID_USED_LAST2 |
| BANKID_USED_LAST3 |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| SUBS_CATEGORY |
| SUBS_TYPE |
| PRODUCT_ID |
| SOURCE_SYSTEM_KEY |
| PRODUCT_NAME |
| BANKID_USED_LAST1 |
| BANKID_USED_LAST2 |
| BANKID_USED_LAST3 |
| FRIFAM_NO_DAYS_ACTIVE |
| FORSIKRING_NO_DAYS_ACTIVE |
| MIN_SKY_NO_DAYS_ACTIVE |
| BINDING_NO_DAYS_ACTIVE |
| BINDING_ACTIVE |
| BINDING_PRODUCT_DESC |
| BINDING_TYPE |
| TERMINAL_BUNDELS |
| DATAKONTR_DOM_NO_DAYS_ACTIVE |
| DATAKONTR_ABR_NO_DAYS_ACTIVE |
| BINDING_PRODUCT_ID |
| BINDING_START_DATE |
| BINDING_END_DATE |
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY_LOG]]


# ADM10_SUBSCRIPTION_HISTORY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure processes historical subscription data for a specified or default monthly period. It constructs a detailed view of subscriptions, including product, user, owner, market area, and binding information, along with calculated active days and duration details. The processed and aggregated data for each month is then stored in a dedicated partition of the `ADM_SUBSCRIPTION_HISTORY` table. The procedure handles the creation of the main history table, its partitions, and associated indexes, and utilizes several temporary tables for intermediate data processing and transformations.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRIMARY_PRODUCT_FLAG |
| PRODUCT_BRAND |
| PRODUCT_DESC |
| PRODUCT_KEY |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| START_DATE |
| SOURCE_SYSTEM_ID |
| BUSINESS_AREA_ID |
| SUBSCRIPTION_ID |
| PARENT_SUBSCRIPTION_ID |
| MAIN_NUMBER |
| KURT_ID_OWNER |
| KURT_ID_USER |
| MARKET_AREA_ID |
| PRODUCT_OFFER_ID |
| PRODUCT_CATEGORY_ID |
| ORIGINAL_START_DATE |
| BINDING_START_DATE |
| BINDING_END_DATE |
| USER_ID |
| INFO_CHG_DATE |
| END_DATE |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| START_DATE |
| BUSINESS_AREA_ID |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| END_DATE |
| PRODUCT_CATEGORY_ID |
| SUBSCRIPTION_SEQ |
| INFO_CHG_DATE |
| SOURCE_SYSTEM_ID |
- ← [[ADM_PRIM_PROD_ATTR_HIST]]
| Column Name |
|---|
| PRODUCT_KEY |
| START_DATE |
| END_DATE |
| PRODUCT_ATTRIBUTE_KEY |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| KURT_ID_USER |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| PRODUCT_OFFER_ID |
| PRODUCT_CATEGORY_ID |
| PRODUCT_BRAND |
| PRODUCT_NAME |
| LAST_PRODUCT_OFFER_ID |
| LAST_PRODUCT_CATEGORY_ID |
| SUBS_NO_DAYS_ACTIVE |
| PROD_NO_DAYS_ACTIVE |
| NO_DAYS_LAST_START |
| NO_DAYS_LAST_CHANGE |
| NO_DAYS_BIND_START |
| NO_DAYS_BIND_END |
| PRODUCT_ATTRIBUTE_KEY |
- → [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_TMP1]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| DAY |
| KURT_ID_OWNER |
| KURT_ID_USER |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| PRODUCT_OFFER_ID |
| PRODUCT_CATEGORY_ID |
| PRODUCT_BRAND |
| PRODUCT_NAME |
| ORIGINAL_START_DATE |
| S_START_DATE |
| SP_START_DATE |
| BINDING_START_DATE |
| BINDING_END_DATE |
| PRODUCT_ATTRIBUTE_KEY |
- → [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_TMP2]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| LAST_PRODUCT_OFFER_ID |
| LAST_PRODUCT_CATEGORY_ID |
| SP2_START_DATE |
- → [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_TMP]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_OWNER |
| KURT_ID_USER |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| PRODUCT_OFFER_ID |
| PRODUCT_CATEGORY_ID |
| PRODUCT_BRAND |
| PRODUCT_NAME |
| LAST_PRODUCT_OFFER_ID |
| LAST_PRODUCT_CATEGORY_ID |
| SUBS_NO_DAYS_ACTIVE |
| PROD_NO_DAYS_ACTIVE |
| NO_DAYS_LAST_START |
| NO_DAYS_LAST_CHANGE |
| NO_DAYS_BIND_START |
| NO_DAYS_BIND_END |
| PRODUCT_ATTRIBUTE_KEY |


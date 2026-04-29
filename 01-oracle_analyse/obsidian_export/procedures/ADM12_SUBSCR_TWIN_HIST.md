# ADM12_SUBSCR_TWIN_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Populates or updates the CRM_ANALYSE.ADM_SUBSCR_TWIN_HIST table by identifying 'twin card' or 'data card' subscriptions and their associated terminal information for a specified month range. It gathers historical subscription details, product attributes, and terminal characteristics from various source systems, including date dimensions, subscription data, product dimensions, and terminal information. The procedure handles table and partition creation if they do not exist, performs data validation, and inserts the processed, cleansed historical data into monthly partitions.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_BRAND |
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
| Column Name |
|---|
| MODELID |
| TACFACID |
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
| Column Name |
|---|
| MODELID |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_OS_TYPE |
| DEVICE_CATEGORY |
| DEVICE_TOUCH_SCREEN |
| DEVICE_TYPE |
| DEVICE_HD_VOICE |
| DEVICE_LTE |
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
| ORIGINAL_START_DATE |
| PRODUCT_OFFER_ID |
| END_DATE |
| INFO_CHG_DATE |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| SUBSCRIPTION_ID |
| TAC_ID |
| IMEI |
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_TWIN_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| MAIN_NUMBER_TWIN |
| SUBSCRIPTION_ID_TWIN |
| KURT_ID_OWNER_TWIN |
| KURT_ID_USER_TWIN |
| MARKET_AREA_ID_TWIN |
| ORIGINAL_START_DATE_TWIN |
| PRODUCT_OFFER_ID_TWIN |
| PRODUCT_NAME_TWIN |
| PRODUCT_BRAND_TWIN |
| TAC_TWIN |
| MODELID_TWIN |
| TERMINAL_USE_FIRST_DATE_TWIN |
| TERMINAL_USE_LAST_DATE_TWIN |
| PRODUCERNAME_TWIN |
| MODELNAME_TWIN |
| DEVICE_OS_TYPE_TWIN |
| DEVICE_CATEGORY_TWIN |
| DEVICE_TOUCH_SCREEN_TWIN |
| DEVICE_TYPE_TWIN |
| DEVICE_HD_VOICE_TWIN |
| DEVICE_LTE_TWIN |


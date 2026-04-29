# V_ANALYTICAL_MASTER_TABLE_TWIN

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, monthly snapshot of subscription history, customer details, and specific 'twin' product/device information for analytical purposes. It links subscriptions to their owners, users, and main numbers, generates monthly keys for various identifiers, and separately extracts device and product offer details for up to three different types of 'twin' services or data cards associated with a subscription. The data is filtered to relevant historical periods (up to the previous month) and excludes certain test/internal customer IDs and customer types/statuses.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_KEY_CHAR |
| LAST_DATE |
- ← [[CLM_ADM.ADM_SUBSCR_TWIN_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| SUBSCRIPTION_ID_TWIN |
| PRODUCT_OFFER_ID_TWIN |
| PRODUCT_NAME_TWIN |
| PRODUCT_BRAND_TWIN |
| TERMINAL_USE_FIRST_DATE_TWIN |
| TERMINAL_USE_LAST_DATE_TWIN |
| MODELID_TWIN |
| MODELNAME_TWIN |
| DEVICE_OS_TYPE_TWIN |
| PRODUCERNAME_TWIN |
| DEVICE_CATEGORY_TWIN |
| DEVICE_TYPE_TWIN |
| DEVICE_HD_VOICE_TWIN |
| DEVICE_TOUCH_SCREEN_TWIN |
| DEVICE_LTE_TWIN |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
| PRODUCT_BRAND |
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| CUSTOMER_SK |
| PERIOD_MONTH_KEY |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCRIPTION_ID_PREV |
| SUBSCRIPTION_ID_ORIG |
| SUBSCRIPTION_ID_PAST |
| MAIN_NUMBER_SK |
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| SUBS_TYPE |


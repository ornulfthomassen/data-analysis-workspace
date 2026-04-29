# VYA_ODS_SUBSCRIPTION_TWIN

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates detailed subscription, product, device (IMEI-based), and mobile usage data for active subscriptions, specifically those identified as 'SIM-kort' products. It provides a comprehensive 'twin' device and usage profile by joining subscription details with product information, device attributes (manufacturer, marketing name, type, usage dates derived from IMEI), and mobile usage metrics for the last 30 days and the preceding three months.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCRIPTION_SEQ |
| PRODUCT_OFFER_ID |
| SUB_NUMBER |
| START_DATE |
| END_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_NAME |
- ← [[LIVE.EUREKA_IMEI]]
| Column Name |
|---|
| IMEI |
| DIRECTORY_NUMBER_ID |
| TERMINAL_USE_LAST_DATE |
| TERMINAL_USE_FIRST_DATE |
| SUBSCR_ID |
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| TAC |
| MANUFACTURER |
| MARKETING_NAME_L1 |
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| MANUFACTURER |
| MARKETING_NAME |
| HANDSET_TYPE |
- ← [[CRM_ANALYSE.ADM_USAGE_MOBILE_TWIN_D30_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUB_NUMBER |
| NET_REVENUE |
| ANT_MMS |
| ANT_SMS |
| ANT_TALE |
| MB_DATA |
| MB_DATA_DOM |
| MB_DATA_PACKAGE_FBB_GARANTI |
- ← [[CRM_ANALYSE.ADM_USAGE_MOBILE_TWIN_MONTH_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUB_NUMBER |
| RELATIVE_MONTH |
| PERIOD_MONTH_KEY |
| NET_REVENUE |
| ANT_MMS |
| ANT_SMS |
| ANT_TALE |
| MB_DATA |
| MB_DATA_DOM |
| MB_DATA_PACKAGE_FBB_GARANTI |


# VYA_ODS_SUBSCRIPTION

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of subscription data, enriching it with customer, product, and handset information, calculating derived metrics such as subscription and product active days, and handling specific business rules for subscription end dates and product reporting categories.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| LOAD_DTTM |
| MARKET_AREA_ID |
| BUSINESS_AREA_ID |
| ACCOUNT_ID |
| SUBSCR_START_DATE |
| PRODUCT_OFFER_ID |
| PRODUCT_OFFER_START_DATE |
| KURT_ID_OWNER |
| KURT_ID_USER |
| KURT_ID_PAYER |
| SUBSCR_END_DATE |
- ← [[CRM_ANALYSE.PD]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_REPORT_LEVEL1 |
| PRODUCT_REPORT_LEVEL2 |
| PRODUCT_REPORT_LEVEL3 |
| PRODUCT_REPORT_LEVEL4 |
| PRODUCT_REPORT_FMC |
| PRODUCT_SALEABLE_FLAG |
| PRODUCT_GROUP |
| PRODUCT_FAMILY_NAME |
| PRODUCT_ACCESS_TYPE_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_SERVICE |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_REPORTING |
| PRODUCT_PORTFOLIO_NAME |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CCDW.SUBSCRIPTION_EXTENSION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| HANDSET_ID_LAST_USED |
| IMEI_LAST_USED |
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIGINAL_START_DATE |
| INFO_REG_DATE |
| PRODUCT_OFFER_ID |
| END_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |


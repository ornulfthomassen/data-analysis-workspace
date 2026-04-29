# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV_3

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and categorizes Broadband (BB) and TV subscription data at a monthly level, considering current and previous periods. It resolves subscription product keys and primary product keys from various source systems (GALAXY, KAS, CCDW), handles specific business rules, location mapping for dual-play services (e.g., Lumino), and identifies Business TV products, presenting them in a unified view.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_NAME_USE |
| PRIMARY_PRODUCT_FLAG |
| SOURCE_SYSTEM_NAME |
| SOURCE_PRODUCT_ID_1 |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_REPORTING |
| DRM_COMMON_SERVICE |
| PRODUCT_END_DATE |
| NBR_ACTIVE_PROD |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| CURRENT_GEOGRAPHY_ID_HOUSE |
| CURRENT_GEOGRAPHY_ID |
| IS_CURRENT |
| IS_APARTMENT |
| LOCATION_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| USER_CUSTOMER_KEY |
| START_DATE |
| END_DATE |
| SOURCE_SUBSCR_ID_1 |
| SUBSCR_USER_LOC_KEY |
| SOURCE_SYSTEM_NAME |
| SUBSCR_CATEGORY_NAME |
| MARKET_AREA_DESC |
| IMEI_FIRST_USED_DT_KEY |
| SUBSCR_FWA_LOC_KEY |
- ← [[KAS.KUNDE]]
| Column Name |
|---|
| ABONNENT_NR |
| ANSVARSTED |
- ← [[KAS.ABONNENTNR_MSISDN]]
| Column Name |
|---|
| ABONNENT_NR |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| SUB_PRODUCT_KEY |
| PRIM_PRODUCT_KEY |
| SUB_PROD_START_DT_KEY |
| SUB_PROD_END_DT_KEY |
| PRIM_PROD_START_DT_KEY |
| PRIM_PROD_END_DT_KEY |
- ← [[CCDW.SUBSCRIBED_PRODUCT_FTV_EXT]]
| Column Name |
|---|
| START_DATE |
| END_DATE |
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| QUANTITY |


# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV2

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and prioritizes fixed broadband (BB) and fixed TV (FTV) subscription data from multiple source systems, including GALAXY, KAS, and CCDW. It generates a monthly view of active subscriptions across four periods (P1, P2, P3, P4) relative to the current date, accounting for complex product relationships, customer locations (Lumino), and specific exclusions (TBB TV). The view provides detailed product keys, subscription keys, source system, and TV type for each subscription at the specified monthly intervals.

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
| IS_CURRENT |
| IS_APARTMENT |
| CURRENT_GEOGRAPHY_ID |
| LOCATION_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| USER_CUSTOMER_KEY |
| START_DATE |
| END_DATE |
| SOURCE_SYSTEM_NAME |
| SUBSCR_CATEGORY_NAME |
| SOURCE_SUBSCR_ID_1 |
| SUBSCR_USER_LOC_KEY |
| MARKET_AREA_DESC |
| IMEI_FIRST_USED_DT_KEY |
- ← [[KAS.KUNDE]]
| Column Name |
|---|
| ABONNENT_NR |
| ANSVARSTED |
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
- ← [[KAS.ABONNENTNR_MSISDN]]
| Column Name |
|---|
| ABONNENT_NR |
- ← [[CCDW.SUBSCRIBED_PRODUCT_FTV_EXT]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| QUANTITY |
- ← [[DUAL]]


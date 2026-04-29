# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates Broadband (BB) and TV subscription data, including primary products, across four different time periods (P1, P2, P3, P4) relative to the current month. It categorizes subscriptions as 'MAIN' or 'Business (BED)', handles special Lumino dual-play scenarios by correlating TV and Broadband subscriptions based on customer and location, and filters out specific TBB (KAS TV) subscriptions. The final output provides monthly period keys, current flags, subscription identifiers, product keys, source systems, TV types, and a count of subscriptions, combining detailed subscription data with aggregated business TV product data.

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
| SOURCE_SYSTEM_NAME |
| SUBSCR_CATEGORY_NAME |
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
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| PRODUCT_OFFER_ID |
| QUANTITY |


# CURRENT_STOCK_POID_QA

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates the 'balance' (likely count of active subscriptions or similar entities) for specific 'Consumerprodukt' subscriptions with 'Abonnement' category and 'Tale' group across various source systems (CM, ODS, GALAXY, CCDW). It identifies each aggregation with a source system identifier ('KILDE'), the product name, and a product offer ID (POID).

## Data Sources (Inputs)
- ← [[CM.REL_NUMBER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SUBSCR_ID_OWNER |
| PRODUCT_END_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_REPORTING |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| PRODUCT_KEY |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| INC_VALID_TO_DATE |
| PRODUCT_OFFER_ID |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| SRC_SUBSCR_PRODUCT_ID |
| PRODUCT_OFFER_ID |
| CUSTOMER_ROLE_ID |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| PRIM_PRODUCT_KEY |
| SUBSCR_QUANTITY |
| SUB_PRODUCT_KEY |
| SUBSCR_TYPE_STATUS_KEY |
| MARKET_AREA_KEY |
| SOURCE_SYSTEM_KEY |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| CURRENT_STATUS |
| SOURCE_SYSTEM_ID |
| MARKET_AREA_ID |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| BUSINESS_AREA_ID |
| END_DATE |
| PRODUCT_OFFER_ID |


# BKV_SUBSCRIPTION_TEST2

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed subscription information, including product details and commercial customer attributes, from multiple dimension and fact tables. It applies specific filtering based on source system, product end date, and checks for null subscription numbers. It also includes conditional logic to standardize commercial customer segment values and determine a primary subscription number based on parent-child relationships within subscriptions, potentially for reporting or analytical purposes related to customer subscriptions.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUB_NUMBER |
| SUBSCRIPTION_KEY |
| PRIM_PRODUCT_KEY |
| OWNER_CUSTOMER_KEY |
| SOURCE_SYSTEM_KEY |
| PRIM_PROD_END_DT_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| MAIN_NUMBER |
| MARKET_AREA_DESC |
| SUBSCRIPTION_KEY |
| PARENT_SUBSCRIPTION_KEY |
| IMEI_LAST_USED |
| IMSI_NUMBER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_BRAND |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_MARKET_PRODUCT_GROUP |
| DRM_COMMON_PAYMENT |
| PRODUCT_KEY |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| COMMERSIAL_CUSTOMER_NAME |
| CURRENT_COMPANY_FAMILY |
| COM_CUSTOMER_SEGMENT |
| COM_CUSTOMER_EMPLOYEES |
| CUSTOMER_KEY |


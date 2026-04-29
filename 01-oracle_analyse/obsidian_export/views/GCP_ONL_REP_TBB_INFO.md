# GCP_ONL_REP_TBB_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed information about specific online service orders, primarily focusing on broadband-related products. It joins service order headers, product details, and subscribed offers, extracting various associated parameters like IMSI, contact phone, email, delivery address, and specific IDs (Kurt, FAR_ID) from generic parameter tables. The view filters for 'New Service' (NS) orders, excludes business customers, and includes products originating from the 'Pacman' system with access types 'FWA' or 'Hjemmebredbånd Mobil'.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_STATUS_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_PROCESSED_DATE |
| DEALER_ID |
| ORDER_ACTION_TYPE_ID |
| CUST_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| SUBSCR_ID |
| ORDER_PHONE_NUM |
| EQ_UNIQUE_NUM |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| PARAM_ID |
| PARAM_VALUE |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| PRODUCT_OFFER_ID |
| PRODUCT_ORDER_LINE_ID |
| OFFER_ORDER_LINE_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_ACCESS_TYPE_NAME |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| OFFER_ORDER_LINE_ID |
| PARAM_ID |
| PARAM_VALUE |


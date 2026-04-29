# V_TM_SALES_ONL

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates online service order data to provide telemarketing sales insights, specifically focusing on new mobile telephony products for consumer customers. It combines information from service orders, products, dealers, and subscribed offers to present an overview of order counts, dealer details, product information (ID, name, monthly price), sales representative, order status, and various order dates for active telemarketing sales channels.

## Data Sources (Inputs)
- ← [[onl_rep.service_order]]
| Column Name |
|---|
| Order_id |
| dealer_id |
| sales_rep_name |
| Order_status_id |
| order_arrival_date |
| order_processed_date |
| cust_type_id |
- ← [[ONL_REP.service_order_product]]
| Column Name |
|---|
| order_id |
| dealer_id |
| PRODUCT_NAME |
| PRODUCT_ACTION_TYPE_ID |
- ← [[galaxy.dealer_dim]]
| Column Name |
|---|
| dealer_name |
| source_dealer_id |
| DRM_SALES_CHANNEL_GEN03_DESC |
| CURRENT_STATUS |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| order_id |
| product_offer_id |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| monthly_price |
| primary_product_flag |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_REPORTING |


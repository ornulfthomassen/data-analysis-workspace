# V_UTVALGTE_ORDRE_CLASSIC

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves specific, filtered order details, product information, customer data, and order status descriptions from a data warehouse. It joins multiple dimension tables with the central order detail fact table, applying extensive filtering conditions based on product names, customer order types, action types, order statuses, market areas, and year-to-date, while excluding certain counterpart classifications.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_DT_DIM_V]]
| Column Name |
|---|
| DAY |
| ORDER_DT_KEY |
| YEAR_TO_DATE |
- ← [[GALAXY.SUBSCR_USER_DIM_V]]
| Column Name |
|---|
| USER_CUSTOMER_KEY |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_DESC |
| ORDER_LINE_PRODUCT_KEY |
- ← [[GALAXY.SALES_ORDER_INDICATOR_DIM_MV]]
| Column Name |
|---|
| CUSTOMER_ORDER_TYPE_DESC |
| ORDER_ACTION_TYPE_DESC |
| ORDER_ACTION_REASON_DESC |
| SALES_ORDER_INDICATOR_KEY |
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_NAME |
| ORDER_STATUS_KEY |
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
| Column Name |
|---|
| ORDER_STATUS_REASON_DESC |
| ORDER_STATUS_REASON_KEY |
- ← [[GALAXY.COUNTERPART_OWNER_DIM_V]]
| Column Name |
|---|
| COUNTERPART_KEY |
| cp_classification_desc |
- ← [[GALAXY.MARKET_AREA_DIM]]
| Column Name |
|---|
| MARKET_AREA_KEY |
| MARKET_AREA_DESC |
- ← [[GALAXY.ORDER_DETAIL_FACT_V]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| ORDER_DT_KEY |
| ORDER_STATUS_REASON_KEY |
| SALES_ORDER_INDICATOR_KEY |
| MARKET_AREA_KEY |
| USER_CUSTOMER_KEY |
| ORDERLINE_PRODUCT_KEY |
| OWNER_CUSTOMER_KEY |
- ← [[GALAXY.SUBSCR_OWNER_DIM_V]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| OWNER_COUNTERPART_KEY |


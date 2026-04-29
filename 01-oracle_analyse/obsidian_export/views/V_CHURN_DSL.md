# V_CHURN_DSL

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates order line data to identify and analyze customer churn activities related to specific DSL (Digital Subscriber Line) products. It filters for particular order types (cancellation, resale), order actions ('CANCELED'), and order statuses ('UPDATED'), excluding certain product categories and customer classifications, for private and business market areas. The view calculates the total number of order lines for these churn-related events, grouped by various time dimensions, main number, user customer key, product details, and order indicators.

## Data Sources (Inputs)
- ← [[ORDER_STATUS_DT_DIM_V]]
| Column Name |
|---|
| DAY |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
| ORDER_STATUS_DT_KEY |
- ← [[SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
- ← [[SUBSCR_USER_DIM_V]]
| Column Name |
|---|
| USER_CUSTOMER_KEY |
- ← [[ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_DESC |
| ORDER_LINE_PRODUCT_KEY |
- ← [[SALES_ORDER_INDICATOR_DIM_MV]]
| Column Name |
|---|
| CUSTOMER_ORDER_TYPE_DESC |
| ORDER_ACTION_TYPE_DESC |
| ORDER_ACTION_REASON_DESC |
| SALES_ORDER_INDICATOR_KEY |
- ← [[ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_NAME |
| ORDER_STATUS_KEY |
- ← [[ORDER_STATUS_REASON_DIM_V]]
| Column Name |
|---|
| ORDER_STATUS_REASON_DESC |
| ORDER_STATUS_REASON_KEY |
- ← [[ORDER_DETAIL_FACT_V]]
| Column Name |
|---|
| NUMBER_OF_ORDER_LINES |
| ORDER_STATUS_KEY |
| ORDER_STATUS_REASON_KEY |
| ORDER_STATUS_DT_KEY |
| PRODUCT_CATEGORY_KEY |
| SALES_ORDER_INDICATOR_KEY |
| MARKET_AREA_KEY |
| USER_CUSTOMER_KEY |
| ORDER_SUBSCR_KEY |
| ORDERLINE_PRODUCT_KEY |
| OWNER_CUSTOMER_KEY |
- ← [[PRODUCT_CATEGORY_DIM_MV]]
| Column Name |
|---|
| PRODUCT_CATEGORY_KEY |
| PRODUCT_CATEGORY_NAME |
- ← [[COUNTERPART_OWNER_DIM_V]]
| Column Name |
|---|
| COUNTERPART_KEY |
| CP_CLASSIFICATION_DESC |
- ← [[MARKET_AREA_DIM]]
| Column Name |
|---|
| MARKET_AREA_KEY |
| MARKET_AREA_DESC |
- ← [[SUBSCR_OWNER_DIM_V]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| OWNER_COUNTERPART_KEY |


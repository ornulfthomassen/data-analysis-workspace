# VYA_TM_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates sales performance metrics (new sales, product changes) for telemarketing channels, enriching the data with product details, order status, dates, dealer information, and sales representative details. The view focuses on consumer product reporting and filters for order dates after 2023.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
| Column Name |
|---|
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_LINE_TYPE_KEY |
| ORDERLINE_PRODUCT_KEY |
| FROM_ORDER_PRODUCT_KEY |
| ORDER_STATUS_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_DT_KEY |
| DEALER_KEY |
| SALES_MATRIX_KEY |
| SOURCE_ORDER_ID |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_REPORTING |
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| MONTHLY_PRICE |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
| Column Name |
|---|
| FROM_ORDER_PRODUCT_KEY |
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| MONTHLY_PRICE |
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| SOURCE_SYSTEM_STATUS_CODE |
| ORDER_STATUS_DESC |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DRM_SALES_CHANNEL_GEN03_DESC |
| DEALER_NAME |
| SOURCE_DEALER_ID |
- ← [[GALAXY.SALES_MATRIX_DIM]]
| Column Name |
|---|
| SALES_MATRIX_KEY |
| SALES_MATRIX_NAME |
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| SALES_REP_NAME |


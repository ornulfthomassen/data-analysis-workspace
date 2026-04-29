# V_MONITOR_PROD_CHANGE_FB

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes and monitors product changes (upsale, downsale, neutral) for mobile telephony subscriptions. It tracks transitions from one product to another, categorizes these changes by sales channel, 'from' and 'to' product family/names, and associates them with a customer's 'Familiebonus' membership status and its activation date. The view aggregates a KPI related to these product changes and provides various date dimensions for analysis.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| KPI_PRODUCT_CHANGE |
| ORDER_DT_KEY |
| ORDERLINE_PRODUCT_KEY |
| FROM_ORDER_PRODUCT_KEY |
| DEALER_KEY |
| ORDER_STATUS_DT_KEY |
| RESOURCE_VALUE |
| market_area_key |
| order_line_type_key |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| TK_PRODUCT_RANK |
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_AREA |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
| Column Name |
|---|
| FROM_ORDER_PRODUCT_KEY |
| PRODUCT_NAME |
| TK_PRODUCT_RANK |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_AREA |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DRM_SALES_CHANNEL_GEN03_DESC |
| DRM_SALES_CHANNEL_GEN04_DESC |
| DRM_SALES_CHANNEL_GEN07_DESC |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |


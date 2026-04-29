# KIM_ORDER_LINE_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_ORDER_LINE_FACT_V`, serves as a comprehensive analytical fact table for order line details. It consolidates data from various dimension and fact tables (e.g., order lines, products, dealers, customers, binding types, market areas, time) to provide a rich dataset for reporting and analysis. Key transformations include deriving order and order status dates/timestamps, classifying products, and calculating Key Performance Indicators (KPIs) such as 'New Sale' and 'Product Change'. The view filters for specific market areas, order statuses, order line types, and excludes certain order line status reasons, focusing on relevant and valid sales-related transactions.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_LINE_ID |
| ORDER_KEY |
| ORDER_LINE_KEY |
| SALES_ORDER_INDICATOR_KEY |
| ORDERLINE_PRODUCT_KEY |
| ORDER_LINE_TYPE_KEY |
| BINDING_TYPE_BENEFIT_KEY |
| BINDING_PRODUCT_KEY |
| BINDED_PRODUCT_KEY |
| BINDING_START_DT_KEY |
| BINDING_END_DT_KEY |
| CUSTOMER_ORDER_ID |
| ORDER_LINE_PARENT_ID |
| ORDER_STATUS_KEY |
| ORDER_STATUS_REASON_KEY |
| FROM_ORDER_PRODUCT_KEY |
| ORDER_SUBSCR_KEY |
| ORDERLINE_SUBSCR_KEY |
| MARKET_AREA_KEY |
| MARKET_AREA_FROM_KEY |
| OWNER_CUSTOMER_KEY |
| USER_CUSTOMER_KEY |
| USER2_CUSTOMER_KEY |
| ORDER_LINE_STATUS_KEY |
| ORDER_LINE_STATUS_REASON_KEY |
| BUSINESS_AREA_KEY |
| DEALER_KEY |
| SOURCE_SYSTEM_KEY |
| HANDSET_KEY |
| ORDER_DT_KEY |
| ORDER_TIME_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_STATUS_TIME_KEY |
| RESOURCE_VALUE |
| SOURCE_ORDER_ID |
- ← [[GALAXY.MARKET_AREA_DIM]]
| Column Name |
|---|
| MARKET_AREA_KEY |
- ← [[GALAXY.MARKET_AREA_FROM_V]]
| Column Name |
|---|
| MARKET_AREA_FROM_KEY |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_BRAND |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_SERVICE |
| PRIMARY_PRODUCT_FLAG |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
| Column Name |
|---|
| FROM_ORDER_PRODUCT_KEY |
- ← [[GALAXY.ORDER_TIME_DIM_V]]
| Column Name |
|---|
| ORDER_TIME_KEY |
| ORDER_TIME |
- ← [[GALAXY.BINDING_PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
| Column Name |
|---|
| BINDING_TYPE_BENEFIT_KEY |
| BINDING_BENEFIT_DESC |
| BINDING_TYPE_DESC |
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
| Column Name |
|---|
| ORDERLINE_TYPE_KEY |
| ORDERLINE_TYPE_CATEGORY_DESC |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DEALER_NAME |
| DRM_SALES_CHANNEL_GEN02_DESC |
| SOURCE_DEALER_ID |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| H_LEVEL |
| SORT_ORDER |


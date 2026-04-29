# VYA_INSIGHT_DEVICE_FROM_ORDER

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "VYA_INSIGHT_DEVICE_FROM_ORDER", consolidates detailed order information related to devices (identified by IMEI). It aggregates various order attributes, such as minimum/maximum source order IDs, market areas, ordering dates, status dates, dealer keys, and device agreement keys. It distinguishes between agreement-specific orders (from mobile and general order line detail fact tables) and service-related orders. The view also enriches the data with customer segmentation by mapping owner and user customer keys, and identifies specific product types (e.g., swap, down payment, insurance, commission) based on product dimension attributes. The primary goal is to provide a comprehensive dataset for device-centric order analysis and insights.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
| Column Name |
|---|
| OWNER_CUSTOMER_KEY |
| USER_CUSTOMER_KEY |
| IMEI |
| SOURCE_ORDER_ID |
| MARKET_AREA_KEY |
| HANDSET_KEY |
| ORDERING_DT_KEY |
| ORDER_STATUS_DT_KEY |
| DEALER_KEY |
| AGREEMENT_KEY |
| KPI_NEWSALE |
| ORDERLINE_PRODUCT_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_STATUS_KEY |
| ORDER_SUBSCR_KEY |
| KPI_PRODUCT_CHANGE |
| TO_ORDER_PRODUCT_KEY |
| FROM_ORDER_PRODUCT_KEY |
| BINDING_PRODUCT_KEY |
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| IMEI |
| SOURCE_ORDER_ID |
| MARKET_AREA_KEY |
| OWNER_CUSTOMER_KEY |
| HANDSET_KEY |
| ORDERING_DT_KEY |
| ORDER_STATUS_DT_KEY |
| DEALER_KEY |
| AGREEMENT_KEY |
| KPI_NEWSALE |
| ORDERLINE_PRODUCT_KEY |
| SOURCE_SYSTEM_KEY |
| ORDER_STATUS_KEY |
| TO_ORDER_PRODUCT_KEY |
- ← [[PRODUCT_DIMENSION]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |


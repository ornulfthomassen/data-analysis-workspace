# VYA_SUBSCR_OUTPORT

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a view of outbound mobile telephony subscription porting activities. It selects open 'utportering' (outporting) order lines for subscriptions with future agreed delivery dates, filtering for specific mobile telephony product categories and market areas.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_SUBSCR_KEY |
| AGREED_DELIVERY_DT_KEY |
| SERVICE_PROVIDER_TO_KEY |
| KPI_PORTING_OUTBOUND |
| ORDERLINE_PRODUCT_KEY |
| MARKET_AREA_KEY |
| ORDER_STATUS_KEY |
| ORDER_LINE_TYPE_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
- ← [[GALAXY.MARKET_AREA_DIM]]
| Column Name |
|---|
| MARKET_AREA_KEY |
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| ORDER_STATUS_CATEGORY_CODE |


# P_ADM_SUBS_USAGE_MONTH_DET_KPI

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates and prepares subscriber usage Key Performance Indicators (KPIs) for a specified month. It creates a temporary table by joining various usage, dimension, and product data, deriving new KPI-related columns based on complex business logic, and drops any pre-existing temporary table with the same name before recreation.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MARKET_AREA_KEY |
| CALL_TYPE_KEY |
| TRAFFIC_TYPE_KEY |
| NETWORK_OPERATOR_KEY |
| ROAMING_COUNTRY_KEY |
| DESTINATION_COUNTRY_KEY |
| PRIM_PRODUCT_KEY |
| DISCOUNT_PRODUCT_OFFER_KEY |
| APN_KEY |
| USAGE_NET_AMOUNT |
- ← [[GALAXY.CALL_TYPE_DIM]]
| Column Name |
|---|
| CALL_TYPE_KEY |
- ← [[GALAXY.ROAMING_COUNTRY_DIM_V]]
| Column Name |
|---|
| ROAMING_COUNTRY_KEY |
| DRM_CURRENT_COUNTRY_GROUPING |
- ← [[GALAXY.DESTINATION_COUNTRY_DIM_V]]
| Column Name |
|---|
| DESTINATION_COUNTRY_KEY |
| DRM_CURRENT_COUNTRY_GROUPING |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_PRODUCT_group |
| SOURCE_SYSTEM_NAME |
| PRODUCT_FAMILY_NAME |
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
| Column Name |
|---|
| TRAFFIC_TYPE_KEY |
| REPORT_GROUP_2 |
| REPORT_GROUP_3 |
| SOURCE_SYSTEM_KEY_3 |
| TRAFFIC_TYPE_NAME_3 |

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_SUBS_USAGE_MONTH_DET_KPI]]
| Column Name |
|---|
| UMDF.* |
| KPI_ROAMING_SONE |
| KPI_DESTINATION_SONE |
| KPI_DESTINATION_SONE_OLD |
| KPI_TRAFFIC_TYPE_L1 |
| KPI_TRAFFIC_TYPE_L2 |
| KPI_DATAPAKKE |
| KPI_SHARED_BUCKET |


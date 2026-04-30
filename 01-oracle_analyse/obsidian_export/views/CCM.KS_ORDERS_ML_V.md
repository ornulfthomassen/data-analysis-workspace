# KS_ORDERS_ML_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts and transforms order-related data from the KS_INTERACTION_ORDERMATCH table. It creates derived identifiers, standardizes main numbers, and calculates Key Performance Indicators (KPIs) such as 'NEWSALE' or 'KPI_PRODUCT_CHANGE' based on specific flags. The data is filtered to include records matching certain ranges for main numbers, positive handle counts, specific product characteristics (Mobil, Abonnement, Tale, Postpaid, Consumerprodukt), or where the SOURCE_ORDER_ID is null. The output is structured for analytical or machine learning purposes.

## Data Sources (Inputs)
- ← [[CCM.KS_INTERACTION_ORDERMATCH]]
| Column Name |
|---|
| START_CAL_DATE |
| CALL_FROM |
| KEYED_NUMBER |
| CALL_FROM_NUM |
| KEYED_NUMBER_NUM |
| KURT_ID_OWNER |
| EMPLOYEE_ID |
| PRODUCT_NAME |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| HANDLE_COUNT |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_REPORTING |
| SOURCE_ORDER_ID |



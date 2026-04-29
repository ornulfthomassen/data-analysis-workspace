# CHURN_CHURN_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies and tracks churn-related events for specific mobile telephony subscriptions by joining various order, product, and status dimensions. It calculates several Key Performance Indicators (KPIs) such as porting outbound and termination, derives a combined churn indicator, and filters for recent events (last 25 months) while ensuring distinctness based on the earliest period month date for unique order, subscription, and event details.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT]]
| Column Name |
|---|
| ORDER_SUBSCR_KEY |
| OWNER_CUSTOMER_SK |
| USER_CUSTOMER_SK |
| KPI_PORTING_OUTBOUND |
| ORDER_KEY |
| ORDER_DT_KEY |
| ORDER_TIME_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_STATUS_TIME_KEY |
| SERVICE_PROVIDER_TO_KEY |
| ORDERLINE_PRODUCT_KEY |
| MARKET_AREA_KEY |
| ORDER_LINE_TYPE_KEY |
| KPI_TERMINATION_SPEECH |
| ORDER_STATUS_KEY |
| ORDER_STATUS_REASON_KEY |
- ← [[GALAXY.ORDER_TIME_DIM_V]]
| Column Name |
|---|
| ORDER_TIME_KEY |
| ORDER_TIME |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_PRODUCT_AREA |
| PRODUCT_FAMILY_NAME |
- ← [[CCDW.SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER_ID |
| SERVICE_PROVIDER_NAME |
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| SOURCE_SYSTEM_STATUS_CODE |
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
| Column Name |
|---|
| ORDERLINE_TYPE_KEY |
| ORDERLINE_TYPE_DESC |
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
| Column Name |
|---|
| ORDER_STATUS_REASON_KEY |
| ORDER_STATUS_REASON_DESC |


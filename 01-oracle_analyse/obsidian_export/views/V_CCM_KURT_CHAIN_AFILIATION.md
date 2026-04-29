# V_CCM_KURT_CHAIN_AFILIATION

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates order and dealer information for customers, providing an overview of their historical engagement with different dealer chains and individual dealers. It calculates various sales-related Key Performance Indicators (KPIs) and identifies the first and last dealer touchpoints for each customer over a two-year period, specifically for sales through physical stores related to 'Tale' (voice) subscriptions.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| SOURCE_ORDER_ID |
| OWNER_CUSTOMER_KEY |
| ORDER_DT_KEY |
| ORDERLINE_PRODUCT_KEY |
| DEALER_KEY |
| BINDING_TYPE_BENEFIT_KEY |
| KPI_NEWSALE |
| HANDSET_KEY |
| KPI_PORTING_INBOUND |
| KPI_PRODUCT_CHANGE |
| KPI_TERMINATION |
| KPI_GROSS_SALE |
| ORDER_STATUS_KEY |
| MARKET_AREA_KEY |
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
| Column Name |
|---|
| ORDER_LINE_PRODUCT_KEY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| PRODUCT_PAYTYPE |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DEALER_CHAIN_NAME |
| DEALER_NAME |
| SOURCE_DEALER_ID |
| DRM_SALES_CHANNEL_TYPE |


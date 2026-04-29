# CHURN_SUBSCR_PROD_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view, `CHURN_SUBSCR_PROD_V`, processes raw subscription product data for churn analysis. It filters for specific sub-product names, standardizes market product categories, calculates the active duration of sub-products within a month, and generates flags indicating if a sub-product started or ended in that month. It also constructs a standardized, unique market sub-product name for aggregated reporting.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCR_PROD_RAW_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| SUB_PRODUCT_START_DATE |
| SUB_PRODUCT_END_DATE |
| SUB_PRODUCT_NAME |
| SUB_PRODUCT_DESC |
| SOURCE_PRODUCT_ID_1 |
| drm_common_market_product |


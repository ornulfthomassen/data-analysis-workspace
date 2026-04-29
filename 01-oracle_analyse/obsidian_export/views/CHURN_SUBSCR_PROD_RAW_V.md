# CHURN_SUBSCR_PROD_RAW_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Provides raw subscription product data, filtered for a 25-month historical window up to the current month, likely for churn analysis. This view selects specific product and subscription-related attributes.

## Data Sources (Inputs)
- ← [[ccm.vya_churn_wide_subscr_products]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| SUB_PRODUCT_START_DATE |
| SUB_PRODUCT_END_DATE |
| DRM_COMMON_MARKET_PRODUCT |
| SUB_PRODUCT_NAME |
| SUB_PRODUCT_DESC |
| SOURCE_PRODUCT_ID_1 |
| period_month |


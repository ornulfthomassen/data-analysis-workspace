# CHURN_SUBS_PROD_CAT_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Aggregates and categorizes various product-related attributes and discounts (e.g., age-based discounts, family discounts, data boosts, free SIMs) for subscriptions on a monthly basis, presenting them as boolean flags or counts.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCR_PROD_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| SUB_PRODUCT_NAME |
| MARKET_PRODUCT |


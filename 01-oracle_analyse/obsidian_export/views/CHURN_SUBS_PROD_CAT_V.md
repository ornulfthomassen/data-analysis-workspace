# CHURN_SUBS_PROD_CAT_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view aggregates and pivots specific subscription product/feature information (such as various discounts, free SIMs, data boosts, and network protection services) into distinct columns. For each combination of 'PERIOD_MONTH_KEY' and 'SUBSCRIPTION_KEY', it quantifies the presence (or count) of these predefined products or features.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_SUBSCR_PROD_V]]


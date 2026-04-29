# VYA_ADM_SUBS_REVENUE

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates and presents detailed subscription revenue information, including various fee types, usage-based revenue, and an adjusted core revenue, by combining subscription revenue data with aggregated subscription usage data for a given period. It specifically handles twin usage and adjusts for discounts.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| BINDING_PRODUCT_KEY |
| NET_INITIATION_FEE |
| NET_DISCOUNT_STARTUP_FEE |
| NET_PERIODIC_FEE |
| NET_DISCOUNT_FIXED_FEE |
| NET_PERIODIC_FEE_BINDING |
| NET_DISCOUNT_FIXED_FEE_BINDING |
| NET_AMOUNT_USE |
| NET_DISCOUNT_AMOUNT_USE |
| NET_REVENUE_ADJUSTED |
| SUBS_PERIOD_START_DATE |
| SUBS_DAYS_ACTIVE_IN_PERIOD |
| SUBS_REVENUE_FACTOR |
| NET_AMOUNT_USE_ROAM |
| NET_DISCOUNT_AMOUNT_USE_ROAM |
| ROAMING_COST_USE |
| NET_AMOUNT_USE_CPA |
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_AGG_V]]
| Column Name |
|---|
| ANT_TWINS_USED |
| NET_REVENUE |
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |


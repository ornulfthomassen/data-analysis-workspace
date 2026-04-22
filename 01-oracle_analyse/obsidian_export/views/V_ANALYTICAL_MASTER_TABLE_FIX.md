# V_ANALYTICAL_MASTER_TABLE_FIX

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`V_ANALYTICAL_MASTER_TABLE_FIX`) serves as a comprehensive analytical master table primarily for fixed-line subscriptions. It aggregates historical subscription details, customer information, product details, voice usage statistics (domestic and international calls, minutes, and costs over three months), and revenue figures for each subscription on a monthly basis. It calculates various derived metrics like total and average voice costs, and identifies fixed-line characteristics such as subscription type and product brands. The view includes filters to exclude specific customer types (only private/consumer customers are included) and known test customers, focusing on historical data up to the previous month.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]


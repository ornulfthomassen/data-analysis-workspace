# V_ANALYTICAL_MASTER_TABLE_DSL

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a comprehensive analytical master table providing monthly snapshots of Digital Subscriber Line (DSL) subscriptions. It aggregates historical data including subscription details, customer information, product characteristics, service activity metrics, and calculated financial (revenue) and usage (voice call) data. The primary purpose is to support CRM analysis by offering a consolidated dataset for understanding DSL subscription lifecycle, customer behavior, and product performance over time, while excluding test customer data.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_DSL_SUBSCR_DETAIL_HIST]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]


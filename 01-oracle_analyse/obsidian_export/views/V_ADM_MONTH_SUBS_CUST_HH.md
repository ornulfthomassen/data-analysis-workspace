# V_ADM_MONTH_SUBS_CUST_HH

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named 'V_ADM_MONTH_SUBS_CUST_HH' in the 'CRM_ANALYSE' schema, consolidates monthly historical data related to subscriptions, customers (both owner and user), and household information. It provides a monthly snapshot of these entities, generating various keys for the current month and the subsequent month, facilitating monthly trend analysis and reporting within a CRM context. It filters out specific test/internal customer records and includes historical data up to the previous month.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]


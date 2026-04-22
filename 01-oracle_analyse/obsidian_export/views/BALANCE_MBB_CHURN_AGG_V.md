# BALANCE_MBB_CHURN_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates historical Mobile Broadband (MBB) subscription data to analyze binding status and potential churn factors over time. It categorizes subscriptions by market (consumer/business), dynamically selects product information based on a migration date (October 2015), and calculates a detailed 'BINDINGSSTATUS' (bound, expiring, out of binding, or unknown) for each period. The view counts the number of subscriptions per combination of these attributes for churn analysis.

## Data Sources (Inputs)
- ← [[ADM_SUBSCR_DETAIL_HIST]]
- ← [[ADM_MBB_SUBSCR_DETAIL_HIST]]


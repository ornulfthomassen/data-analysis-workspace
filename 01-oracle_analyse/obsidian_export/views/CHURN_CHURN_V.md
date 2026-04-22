# CHURN_CHURN_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view is designed to identify and consolidate customer churn events, specifically focusing on mobile telephony subscriptions with 'Abonnement' product categories and 'Postpaid' payment types. It calculates various Key Performance Indicators (KPIs) related to termination and porting outbound based on order line details. The view filters for recent events (within the last 25 months) and uses window functions to select the first recorded churn event for a given order within a specific month, effectively de-duplicating or prioritizing events for monthly churn analysis. It derives monthly period dates for reporting.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SERVICE_PROVIDER]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]


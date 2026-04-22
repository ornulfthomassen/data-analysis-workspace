# V_SUBSCRIPTION_ORDER_STATUS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated status for subscriptions, specifically focusing on recent 'Change' or 'Porting' related service order activities. It retrieves core subscription details and then attempts to determine if a subscription is currently undergoing or has recently completed a change or porting process, based on service order data from the last 6 hours. The output includes subscription identifiers and a descriptive order status (e.g., 'CHANGE IN PROGRESS', 'PORTING COMPLETED').

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]


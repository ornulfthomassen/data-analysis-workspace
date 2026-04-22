# V_MPORT_REALTIME

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named V_MPORT_REALTIME, is designed to provide real-time or near real-time information on mobile number porting (MNP) orders. It aggregates various details about service orders, associated products, subscriptions, and their specific parameters (such as IMEI, 'to' and 'from' service providers, and the actual porting date). It filters for specific customer types, recent orders (within approximately the last 7 hours), and a particular product offer category (ID 10), likely corresponding to porting-related offers. The output includes key identifiers, statuses, product information, timestamps, and aggregated parameter values.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
- ← [[CM.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]


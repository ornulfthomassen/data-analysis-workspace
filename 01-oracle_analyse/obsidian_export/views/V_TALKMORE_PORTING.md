# V_TALKMORE_PORTING

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates the volume of distinct service orders related to mobile number porting activities (Port-In and Port-Out) specifically involving service provider '705' (which the view name suggests is 'Talkmore'). The data is grouped by the 'from' and 'to' service providers, order arrival date, product action type, order status, and customer type, for orders placed on or after January 1, 2022.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
- ← [[CCDW.SERVICE_PROVIDER]]


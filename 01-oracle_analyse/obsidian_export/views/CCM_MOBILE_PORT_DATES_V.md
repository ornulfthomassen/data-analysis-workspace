# CCM_MOBILE_PORT_DATES_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of mobile number porting order details, including upcoming/in-progress and recently completed porting events, along with related subscription and service provider information. It tracks porting dates, calculates days until port, and filters orders based on status, action type, and specific porting parameters.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]


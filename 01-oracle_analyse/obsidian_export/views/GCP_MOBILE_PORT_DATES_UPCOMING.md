# GCP_MOBILE_PORT_DATES_UPCOMING

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated list of upcoming mobile number porting orders, categorizing them as either 'outporting' (Utportering) or 'inporting' (Innportering). It details the origin and destination service providers (Telenor, Talkmore, or External) for each port, and calculates the number of days remaining until the porting execution date. The data is filtered to include only orders with specific statuses ('IB', 'UB') and action types, with a focus on orders scheduled to execute from yesterday onwards. It distinguishes between Telenor and Talkmore customers and provides relevant order, customer, and subscription details where available.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_CUSTOMER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[GALAXY.PRODUCT_DIM]]


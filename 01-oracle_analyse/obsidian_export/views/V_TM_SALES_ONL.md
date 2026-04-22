# V_TM_SALES_ONL

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and retrieves telemarketing sales order details, including distinct order counts, dealer information, product details (specifically for 'Mobil Telefoni' consumer products with new subscriptions), sales representative names, and various order dates and statuses. The data is grouped by dealer, product, sales rep, order status, monthly price, and order dates, providing a detailed view of sales performance and order characteristics within the telemarketing channel for private customers.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[GALAXY.PRODUCT_DIM]]


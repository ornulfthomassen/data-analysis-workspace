# ONL_ORDERS_20131022_TODAY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated dataset of online orders placed or loaded since October 22, 2013. It enriches the order information from the 'onl_orders' table with details from active customer subscriptions by joining on the order's phone number and the subscription's main number. The view captures a wide range of attributes related to orders, products, customers, contracts, and various operational details.

## Data Sources (Inputs)
- ← [[onl.onl_orders]]
- ← [[CCDW.SUBSCRIPTION]]


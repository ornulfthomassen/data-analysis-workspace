# UPSALE_KS_INTERA_KURT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines detailed customer interaction data with product order line information, specifically focusing on product change orders. Its main purpose is to link orders where a product change occurred (KPI_PRODUCT_CHANGE = 1) with subsequent customer interactions (interactions happening after the order's status date). It appears to be designed for analyzing customer engagement or potential upsell opportunities following a product change, by relating past orders to later interactions, while excluding interactions directly associated with the main number of the product change order.

## Data Sources (Inputs)
- ← [[CLM_KIM.ORDER_LINE_REP1]]
- ← [[CRM_ANALYSE.KS_INTERACTION]]


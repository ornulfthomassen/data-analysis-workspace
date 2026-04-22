# VIYA_TM_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and categorizes sales and order activities into specific Key Performance Indicators (KPIs): 'New Sales/Product Initiation' (KPI_NYSALG), 'Product Change' (KPI_PRODUCT_CHANGE), and 'Owner Change' (KPI_OWNERCHANGE). It combines service order details with product information from a product dimension, filtering for specific dealers and recent orders (from 2021 onwards). The view focuses on orders that have at least two specific product line items and a 'New' action type for a particular product offer category (ID 20).

## Data Sources (Inputs)
- ← [[onl_rep.service_order]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[GALAXY.PRODUCT_DIM]]


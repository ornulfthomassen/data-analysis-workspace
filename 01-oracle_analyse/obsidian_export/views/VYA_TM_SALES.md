# VYA_TM_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates aggregated Key Performance Indicators (KPIs) for 'New Sales' and 'Product Change' within a telemarketing context. It provides a detailed breakdown of these KPIs by various dimensions including product attributes (name, ID, monthly price, area, category, primary flag), order details (line type, status, dates), sales representative, dealer information, and sales matrix. The data is specifically filtered for 'Consumerprodukt' products and 'Telemarketing' sales channels, including orders placed after the year 2023.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.SALES_MATRIX_DIM]]
- ← [[ONL_REP.SERVICE_ORDER]]


# GCP_TM_SALES

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides aggregated Telemarketing (TM) sales data for consumer products, calculating Key Performance Indicators (KPIs) like new sales and product changes. It combines detailed information about orders, products, order statuses, dealers, and sales representatives. The data is filtered for the 'Telemarketing' sales channel, 'Consumerprodukt' product types, and orders from 2023 onwards, intended for reporting in Google Cloud Platform (specifically GCP Looker).

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.SALES_MATRIX_DIM]]
- ← [[ONL_REP.SERVICE_ORDER]]


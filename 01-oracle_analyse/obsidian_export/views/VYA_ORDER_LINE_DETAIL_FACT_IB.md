# VYA_ORDER_LINE_DETAIL_FACT_IB

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides detailed order line information, primarily by selecting all columns from the `VYAMN_ORDER_LINE_DETAIL_FACT` table. It filters these order lines to include only those associated with the 'MOBILE' business area and an 'OPEN' order status category, joining with the `ORDER_STATUS_DIM_MV` to apply these filters. The view likely serves as a curated fact table for analytical reporting on active (open) mobile order line details, including various Key Performance Indicators (KPIs) related to sales, churn, product changes, and device swaps.

## Data Sources (Inputs)
- ← [[CCM.VYAMN_ORDER_LINE_DETAIL_FACT]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]


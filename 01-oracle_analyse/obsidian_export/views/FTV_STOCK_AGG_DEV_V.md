# FTV_STOCK_AGG_DEV_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, FTV_STOCK_AGG_DEV_V, calculates and aggregates a comprehensive set of Key Performance Indicators (KPIs) related to product stock, customer movements (growth and churn), and product attribute changes over time. It provides metrics such as opening and closing balances, net changes, various types of 'tilvekst' (growth/additions) and 'churn' (disconnections), and transitions between product combinations (e.g., Dualplay, Broadband Only, TV Only) and technologies (e.g., Coax to Fiber). The view integrates product and time dimensions, ensuring that data is available for all relevant months and dwelling unit types (MDU, SDU, BED) by generating a complete time series and joining it with the aggregated stock data.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCM.FTV_STOCK_BASE]]
- ← [[ccm.FTV_PRODUCT_BB_V_TMP]]


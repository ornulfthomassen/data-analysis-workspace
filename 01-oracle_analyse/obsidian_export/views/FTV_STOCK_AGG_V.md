# FTV_STOCK_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, FTV_STOCK_AGG_V, provides a comprehensive, monthly aggregated report of various Key Performance Indicators (KPIs) related to product stock, subscriber movements (growth/acquisition, churn), and product changes (e.g., speed, technology, subscription type, and product combinations like Dualplay, BB Only, TV Only). It combines detailed product attributes with monthly balance and movement figures, allowing for analysis of subscriber base evolution across different dwelling unit types (MDU, SDU, BED) and product hierarchies. The view includes historical data starting from 2022 to the current year, ensuring that all month-dwelling unit type combinations within this period are represented, even if specific KPI data is not available for every combination.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCM.FTV_STOCK_BASE]]
- ← [[ccm.FTV_PRODUCT_BB_V_TMP]]
- ← [[DUAL]]


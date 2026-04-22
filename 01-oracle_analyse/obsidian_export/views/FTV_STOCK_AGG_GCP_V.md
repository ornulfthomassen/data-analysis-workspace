# FTV_STOCK_AGG_GCP_V

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view calculates a comprehensive set of Key Performance Indicators (KPIs) related to telecommunication product stock, customer growth (tilvekst), churn, and various product changes (e.g., speed upgrades/downgrades, technology migrations like Coax to Fiber, and subscription type changes). It provides detailed historical (monthly) insights into opening and closing balances for broadband (BB), TV, dualplay, BB-only, and TV-only subscriptions, enriched with product attributes (name, area, group, category, technology, speed, dwelling unit type) and source system information. It aggregates data to show net changes, total changes, and specific types of growth and churn events, often differentiating between current and previous product states.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_STOCK_EQV_V4]]
- ← [[ccm.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.DATE_DIM_MV]]


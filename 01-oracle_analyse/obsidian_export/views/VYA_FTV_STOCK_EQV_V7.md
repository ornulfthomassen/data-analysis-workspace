# VYA_FTV_STOCK_EQV_V7

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates detailed Key Performance Indicators (KPIs) related to customer subscription stock, opening and closing balances, net changes, churn, and growth (Tilvekst) for various product combinations (Broadband, TV, Dualplay), speeds, and technologies. It provides a comprehensive, monthly breakdown of product-related movements and states, including technology changes (e.g., Coax to Fiber), product changes, and subscription type changes, enriched with extensive product and date dimension attributes.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_STOCK_EQV_V3]]
- ← [[ccm.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.DATE_DIM_MV]]


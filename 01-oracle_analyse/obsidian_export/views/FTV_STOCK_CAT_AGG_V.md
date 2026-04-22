# FTV_STOCK_CAT_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view enriches and consolidates product stock and subscription change data by joining base stock records with detailed product attributes and date dimensions. It calculates various product-specific characteristics (e.g., dwelling unit type, technology, speed, reporting, subscription type) for both opening and closing balances, and for different product types (broadband, TV, primary product). It also includes flags and categories to track churn, new customer acquisitions, and product combination changes, providing a comprehensive dataset for analyzing customer movements and product inventory over time.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_BASE_V2]]
- ← [[ccm.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.DATE_DIM_MV]]


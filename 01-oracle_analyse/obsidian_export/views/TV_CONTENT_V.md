# TV_CONTENT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches product-related information, specifically focusing on 'Content' type products from the 'KAS' source system. It joins data from a product dimension table, a product staging table, and a Qlikview-related product table to provide detailed content attributes such as product key, category, name, type, and vendor. It also standardizes some identifier formats and vendor names.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CVIEW_STAGING.PRODUCT]]
- ← [[QLIKVIEW.PRODUCT]]


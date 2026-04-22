# PRODUCT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, PRODUCT_DIM_V, serves as a comprehensive product dimension. Its primary purpose is to consolidate and standardize a wide range of product attributes from various source systems into a single, unified view. It includes detailed product classifications (e.g., reporting levels, technology, category, group), pricing and inclusion details (e.g., startup fees, monthly fees, included minutes/SMS/MB), and other descriptive characteristics. The view combines general product data with specific product data related to 'Talkmore' offerings, applying business logic and transformations (such as CASE statements for product reporting levels and technology classification) to create a consistent master data set for products, likely used for analytical reporting, CRM, and business intelligence.

## Data Sources (Inputs)
- ← [[PD]]
- ← [[CLM_ADM.TALKMORE_PRIM_PRODUCT_DIM]]


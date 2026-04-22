# KIM_ORDER_MATCH_PRODUCT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates product master data with hierarchical product type configuration details. It extracts various product attributes like name, category, reporting group, technology, payment type, brand, and service from the `PRODUCT_DIM` table, and then enriches this data by joining with `CCM_PRODUCT_TYPE_CONFIG` to include product type parentage and descriptions. This comprehensive product dimension is likely used for CRM analysis, order matching, or other business intelligence purposes requiring detailed and structured product information.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


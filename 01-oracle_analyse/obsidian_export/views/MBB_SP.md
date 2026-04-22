# MBB_SP

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines detailed information about subscribed products from `CCDW.SUBSCRIBED_PRODUCT` with product type configuration data from `CLM_CCM.CCM_PRODUCT_TYPE_CONFIG`. It enriches the subscribed product records by fetching the product name and its parent description based on specific product categories/types defined by the `PTC.PARENT IN (...)` clause, providing a consolidated view of subscribed products with their descriptive attributes for CRM analysis.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


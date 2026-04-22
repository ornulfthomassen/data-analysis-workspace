# MPR_SP

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `MPR_SP`, enriches subscribed product information by joining `CCDW.SUBSCRIBED_PRODUCT` with product configuration details from `CLM_CCM.CCM_PRODUCT_TYPE_CONFIG`. It retrieves product names and descriptions, specifically filtering for product types whose parent IDs are within a predefined set (2, 43, 49, 57, 58, 59). The output provides a comprehensive view of subscribed products with their descriptive details.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


# MPR_S

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive list of subscriptions. It enriches the core subscription data from the 'CCDW.SUBSCRIPTION' table by joining with the 'CLM_CCM.CCM_PRODUCT_TYPE_CONFIG' table twice. The first join (`PTC`) brings in the 'PRODUCT_NAME' and applies a filter on specific parent product categories (2, 43, 49, 57, 58, 59). The second join (`PTCP`) retrieves the 'DESCRIPTION' of these parent product categories. Essentially, it links individual subscriptions to their product offerings and their respective product type hierarchy (product name and parent description).

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


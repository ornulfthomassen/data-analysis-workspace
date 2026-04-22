# SUBS_SP

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides an enriched and consolidated view of subscribed products. It combines core subscription details (like IDs, dates, fees, and resource values) from the `SUBSCRIBED_PRODUCT` table with product descriptive information (`GALAXY_PROD_NAME`) from `GALAXY.PRODUCT_DIM` and product type configuration details (`PRODUCT_NAME`, `DESCRIPTION`) from `CLM_CCM.CCM_PRODUCT_TYPE_CONFIG`. The view serves to present a comprehensive snapshot of subscriptions with expanded product context for analysis.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


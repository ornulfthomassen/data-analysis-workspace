# MBB_S

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates comprehensive subscription details from the `SUBSCRIPTION` table and enriches them with product names and descriptions by joining with `PRODUCT_DIM` and two instances of `CCM_PRODUCT_TYPE_CONFIG`. It likely aims to provide a unified dataset for analyzing subscriptions, product categories, and their related attributes, potentially filtered by specific product parent categories (3, 25, 35, 63).

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


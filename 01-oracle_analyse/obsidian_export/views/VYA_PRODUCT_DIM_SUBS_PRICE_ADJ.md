# VYA_PRODUCT_DIM_SUBS_PRICE_ADJ

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves and categorizes product-specific price adjustments and discount information. It calculates and distinguishes between price overrides, absolute price reductions, and percentage-based price reductions based on product offer configuration data. This information is then linked to product dimensions, and the view also includes placeholder products for special cases.

## Data Sources (Inputs)
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]


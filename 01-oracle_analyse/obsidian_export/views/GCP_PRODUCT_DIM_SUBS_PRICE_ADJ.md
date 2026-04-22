# GCP_PRODUCT_DIM_SUBS_PRICE_ADJ

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and categorizes product price adjustments and discounts. It extracts adjustment details (override price, price reduction in absolute value and percentage) from product offer configurations based on specific configuration IDs (e.g., for age, family, or other discounts). These adjustments are then linked to product master data from the product dimension table. The view also includes specific default product keys with zero adjustments. Its primary purpose is to prepare and load product price reduction/override data for reporting or integration into other systems.

## Data Sources (Inputs)
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]
- ← [[PCAT.PRODUCT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]


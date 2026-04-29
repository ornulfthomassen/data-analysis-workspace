# GCP_PRODUCT_DIM_SUBS_PRICE_ADJ

**Schema:** `CCM` | **Type:** `View`

## Description
The view `GCP_PRODUCT_DIM_SUBS_PRICE_ADJ` consolidates product price adjustment (discounts, overrides) information by combining product configuration data from PCAT schema with product dimension details from GALAXY.PRODUCT_DIM. It calculates various types of price adjustments (override price, price reduction, percentage reduction) based on configuration parameters and links them to specific products. The view also includes specific placeholder product keys for scenarios like 'no discount' or 'unknown discount'. Its primary purpose is to prepare and load price reduction/override data into the 'Mjøsa' system.

## Data Sources (Inputs)
- ← [[PCAT.V_PRODUCT_OFFER_CONFIG_MV]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| CONFIGURATION_ID |
| CONFIGURATION_VALUE |
| CONFIGURATION_VALUE_DESCR |
- ← [[PCAT.PRODUCT_OFFER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| PUBLIC_NAME |
| PRODUCT_OFFER_CATEGORY_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_REPORTING |
| PRODUCT_NAME |


# VYA_PRODUCT_DIM_SUBS_PRICE_ADJ

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates and presents product-specific price adjustments, overrides, and discount types by aggregating product offer configurations and enriching them with product dimension data. It also includes special product keys (-1, -2) for reporting purposes, particularly for 'Fastpris redusert' (Fixed Price Reduced) mobile telephony products from the 'Pacman' system.

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
| PRODUCT_NAME |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_REPORTING |


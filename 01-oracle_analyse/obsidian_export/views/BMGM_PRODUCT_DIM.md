# BMGM_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view, "BMGM_PRODUCT_DIM", consolidates and categorizes product information from the "GALAXY.PRODUCT_DIM" table. It processes product data from various source systems (Pacman, deFakto, KAS) and assigns a 'ROLLE' (USER or OWNER) to each product. Furthermore, it generates binary flags (0 or 1) to classify products into specific subscription types such as private postpaid, business postpaid, swap agreements, mobile broadband, fixed broadband, and fixed telephony, based on their attributes like product area, category, pay type, and reporting segment. The view provides a standardized product dimension for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_REPORTING |
| PRODUCT_PAYTYPE |
| PRODUCT_NAME |


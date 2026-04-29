# TMP_BMGM_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view aggregates and categorizes product information from the `GALAXY.PRODUCT_DIM` table. It combines product data from different source systems ('Pacman', 'deFakto', 'KAS') and applies business rules to assign product roles ('USER', 'OWNER') and calculate various subscription metrics (e.g., private postpaid, swap agreements, business postpaid, mobile broadband, fixed broadband, fixed telephony subscriptions) based on product attributes like area, category, and payment type. The view aims to provide a consolidated product dimension for reporting and analysis, distinguishing between different types of product usage and ownership.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_PAYTYPE |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_REPORTING |
| PRODUCT_NAME |


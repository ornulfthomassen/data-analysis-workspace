# FTV_PRODUCT_BB_V_TMP

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a classified and enriched list of broadband and TV products, deriving attributes like subscription type, dwelling unit type, product speed, technology, and priority from various product properties and system sources. It consolidates product information for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| DRM_COMMON_TECHNOLOGY |
| PRIMARY_PRODUCT_FLAG |
| PRODUCT_KEY |
| PRODUCT_NAME_USE |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_ACTIVE_FLAG |
| DRM_COMMON_SERVICE |
| NBR_ACTIVE_PROD |
| NBR_ACTIVE_PROD_BUSINESS |
| NBR_ACTIVE_PROD_CONSUMER |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_BRAND |
| DRM_COMMON_PORTFOLIO |
| DRM_COMMON_PAYMENT |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_REPORTING |
| BAUD_UPLOAD |
| BAUD_DOWNLOAD |
- ← [[KAS.PRODUKT]]
| Column Name |
|---|
| PRODUKT_NR |
| PRODUKT_NAVN |
| HASTIGHETSPRODUKT |
| KOMPLETT |


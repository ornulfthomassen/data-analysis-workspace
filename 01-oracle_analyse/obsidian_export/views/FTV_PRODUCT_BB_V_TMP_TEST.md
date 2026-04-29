# FTV_PRODUCT_BB_V_TMP_TEST

**Schema:** `CCM` | **Type:** `View`

## Description
The view `FTV_PRODUCT_BB_V_TMP_TEST` consolidates and categorizes product information, primarily focusing on broadband (BB) and TV products. It derives various product attributes such as subscription type, dwelling unit type, technology, value chain, product priority, and source tags by applying complex business rules and data transformations based on product names, IDs, and system origins. It also standardizes speed metrics and enriches dwelling unit type information for specific 'Komplett' (package) products from the `KAS.PRODUKT` table, ultimately providing a comprehensive and categorized view of products.

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
| DRM_COMMON_PRODUCT_AREA |
| PRODUCT_END_DATE |
| NBR_ACTIVE_PROD |
| DRM_COMMON_SERVICE |
| DRM_COMMON_REPORTING |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_ACTIVE_FLAG |
| NBR_ACTIVE_PROD_BUSINESS |
| NBR_ACTIVE_PROD_CONSUMER |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_BRAND |
| DRM_COMMON_PORTFOLIO |
| DRM_COMMON_PAYMENT |
| PRODUCT_START_DATE |
| BAUD_UPLOAD |
| BAUD_DOWNLOAD |
- ← [[KAS.PRODUKT]]
| Column Name |
|---|
| PRODUKT_NR |
| PRODUKT_NAVN |
| HASTIGHETSPRODUKT |
| KOMPLETT |


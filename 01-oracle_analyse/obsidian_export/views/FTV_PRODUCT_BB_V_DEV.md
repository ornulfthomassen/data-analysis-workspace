# FTV_PRODUCT_BB_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and categorizes product information, primarily for Broadband and TV services, from the GALAXY.PRODUCT_DIM table across multiple source systems (KAS, deFakto, Pacman). It derives specific attributes like SUBSCRIPTION_TYPE, DWELLING_UNIT_TYPE, and PRODUCT_PRIORITY based on business rules applied to product characteristics, providing a unified and enriched product dimension view. It also includes a hardcoded dummy TV product entry.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_NAME_USE |
| PRIMARY_PRODUCT_FLAG |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_BRAND |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PORTFOLIO |
| DRM_COMMON_SERVICE |
| DRM_COMMON_PAYMENT |
| BAUD_UPLOAD |
| BAUD_DOWNLOAD |
| NBR_ACTIVE_PROD_CONSUMER |
| NBR_ACTIVE_PROD_BUSINESS |
| NBR_ACTIVE_PROD |
| PRODUCT_ACTIVE_FLAG |
- ← [[DUAL]]


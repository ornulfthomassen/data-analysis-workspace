# V_CCM_DRM_PROD_GPD

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts general product data (GPD) from the `PRODUCT_DIM` table, specifically filtering for products originating from the 'Pacman' source system. It renames the `SOURCE_PRODUCT_ID_1` column to `POID` and provides a wide range of product-related attributes, including identifiers, names, descriptions, classification details, dates, pricing, data inclusions, active product counts for consumer and business segments, and saleability across various platforms.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_NAME |
| PRODUCT_DESC |
| DRM_PRODUCT_CLASS |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| DRM_COMMON_BRAND |
| DRM_COMMON_REPORTING |
| DRM_COMMON_SERVICE |
| DRM_COMMON_PAYMENT |
| PRODUCT_CATEGORY_ID |
| PRODUCT_CATEGORY_NAME |
| PRODUCT_PORTFOLIO_NAME |
| PRODUCT_FAMILY_NAME |
| PRODUCT_PAYMENT_TYPE_NAME |
| MONTHLY_PRICE |
| INCLUDED_DATA |
| NBR_ACTIVE_PROD_CONSUMER |
| NBR_ACTIVE_PROD_BUSINESS |
| SOURCE_SYSTEM_NAME |
| SALEABLE_IN_PAD |
| SALEABLE_IN_EUREKA |
| SALEABLE_IN_MINE_SIDER |
| SALEABLE_IN_MONA_MITT_TELENOR |


# MISSING_DRM_REP_BRAND_PAY

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies products in `GALAXY.PRODUCT_DIM` that have missing Digital Rights Management (DRM) related attributes (Reporting, Brand, Payment, Technology, Product Category, Product Group), categorizes the type of missing DRM information, and retrieves the most recent associated treatment details from `CRM_ANALYSE.KIM_TREATMENT_DIM` for these products.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_SK |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
| TREATMENT_KEY |
| TREATMENT_CD |
| TREATMENT_NM |
| TREATMENT_DESC |
| TREATMENT_PRODUCT_DESC |
| BRAND |
| KPI_TYPE |
| ACTION_CATEGORY |
| ACTION_CATEGORY_TYPE |
| OFFER_CATEGORY |
| HANDSET_KEY |
| PRODUCT_KEY_5 |
| PRODUCT_KEY_6 |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_NAME |
| PRODUCT_DESC |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_REPORTING |
| DRM_COMMON_BRAND |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_TECHNOLOGY |
| SOURCE_SYSTEM_NAME |


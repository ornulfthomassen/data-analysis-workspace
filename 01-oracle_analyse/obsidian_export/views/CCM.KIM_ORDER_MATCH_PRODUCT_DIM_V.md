# KIM_ORDER_MATCH_PRODUCT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a product dimension view by joining product details from 'PRODUCT_DIM' with hierarchical product type configuration information from 'CCM_PRODUCT_TYPE_CONFIG', including parent product type descriptions.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| product_name |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_BRAND |
| DRM_COMMON_SERVICE |
| PRIMARY_PRODUCT_FLAG |
| PRODUCT_FAMILY_NAME |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| H_LEVEL |
| DESCRIPTION |



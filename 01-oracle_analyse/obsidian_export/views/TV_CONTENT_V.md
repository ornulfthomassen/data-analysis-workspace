# TV_CONTENT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, TV_CONTENT_V, consolidates product information from multiple sources to create a unified view of TV content. It joins product dimensions from 'GALAXY.PRODUCT_DIM' with product details from 'CVIEW_STAGING.PRODUCT', filtering for specific source systems and product types. It also incorporates content names from 'QLIKVIEW.PRODUCT' and standardizes vendor names.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_CATEGORY_NAME |
| PRODUCT_NAME |
| SOURCE_SYSTEM_NAME |
- ← [[CVIEW_STAGING.PRODUCT]]
| Column Name |
|---|
| LEGACY_PRODUCT_ID__C |
| PRODUCT_TYPE__C |
| PRODUCT_SUBTYPE__C |
| PPC_PRODUCT_ID__C |
| DESCRIPTION |
| ID |
- ← [[QLIKVIEW.PRODUCT]]
| Column Name |
|---|
| ID |
| NAME |


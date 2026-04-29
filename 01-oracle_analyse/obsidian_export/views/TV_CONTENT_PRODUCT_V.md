# TV_CONTENT_PRODUCT_V

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and enriches TV content product information from various staging and Qlikview sources, categorizing products into channels, packages, and basic packages, providing a unified view with standardized attributes and validity periods. It combines dynamically sourced product data with a fallback to static product definitions where dynamic data is absent.

## Data Sources (Inputs)
- ← [[CVIEW_STAGING.PRODUCT]]
| Column Name |
|---|
| LEGACY_PRODUCT_ID__C |
| PPC_PRODUCT_ID__C |
| PRODUCT_SUBTYPE__C |
| DESCRIPTION |
| PRODUCT_VALID_FROM__C |
| PRODUCT_VALID_TO__C |
| ID |
| PRODUCTCODE |
| NAME |
- ← [[QLIKVIEW.PRODUCT]]
| Column Name |
|---|
| ID |
| NAME |
| PPC_PRODUCT_ID__C |
| CREATEDDATE |
- ← [[CVIEW_STAGING.PACKAGE_PRODUCT]]
| Column Name |
|---|
| PRODUCT_PPC_ID__C |
| PARENT_PRODUCT_PPC_ID__C |
| VALID_FROM_DATE__C |
| VALID_TO_DATE__C |
| PARENT_PRODUCT__C |
| PRODUCT__C |
- ← [[KAS.PRODUKT]]
| Column Name |
|---|
| PRODUKT_NR |
- ← [[QLIKVIEW.TVCONTENTPRODUCT]]
| Column Name |
|---|
| PRODUCT_NR |
| CONTENT_ID |
| CONTENT_NAME |
| SEGMENT |
| CONTENT_GRP |
| VENDOR |
| PACKAGE_GRP |


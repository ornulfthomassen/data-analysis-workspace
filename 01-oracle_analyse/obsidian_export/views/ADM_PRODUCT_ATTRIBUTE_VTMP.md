# ADM_PRODUCT_ATTRIBUTE_VTMP

**Schema:** `CCM` | **Type:** `View`

## Description
The view transforms and standardizes raw product attribute data from the GALAXY.PRODUCT_DIM table. It cleanses and converts various pricing (e.g., startup, monthly fees, after-included prices), usage (e.g., included minutes, SMS, MMS, MB), and technical specifications (e.g., baud rates, baud reduction quota) from string formats to numerical values. Additionally, it enriches the product data with hierarchical product type information by joining with the CLM_CCM.CCM_PRODUCT_TYPE_CONFIG table, and filters out products from a specific source system.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
| PRODUCT_PAYTYPE |
| PRIMARY_PRODUCT_FLAG |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
| SOURCE_SYSTEM_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_PRODUCT_ID_2 |
| DRM_COMMON_BRAND |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_REPORTING |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PORTFOLIO |
| DRM_COMMON_SERVICE |
| ESTABLISHMENT_PRICE |
| MONTHLY_PRICE |
| PRICE_VAT_DESC |
| INCLUDED_MINUTES |
| INCLUDED_SMS |
| PRICE_SMS_AFTER_INCLUDED |
| INCLUDED_MMS |
| PRICE_MMS |
| INCLUDED_DATA |
| PRICE_DATA_AFTER_INCLUDED |
| MAX_MONTHLY_DATA_CHARGE |
| BAUD_UPLOAD |
| BAUD_DOWNLOAD |
| BAUD_REDUCTION_QUOTA |
| TK_PRODUCT_RANK |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| DESCRIPTION |


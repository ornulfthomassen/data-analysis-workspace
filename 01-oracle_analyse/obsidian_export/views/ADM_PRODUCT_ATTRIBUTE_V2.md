# ADM_PRODUCT_ATTRIBUTE_V2

**Schema:** `CCM` | **Type:** `View`

## Description
This view processes raw product dimension data to create a comprehensive and cleaned view of product attributes. It standardizes various string-based price, usage, and bandwidth attributes into numerical formats, often performing data cleaning, unit conversions (e.g., KB to MB), and conditional logic. Additionally, it enriches the product information with hierarchical product type details by joining with product configuration tables. The view filters out products from the 'Marius' source system.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
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


# GCP_ADM_PRODUCT_ATTRIBUTE_HIST_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a monthly historical snapshot of product attributes. It joins a month dimension table with a historical product attribute table to associate each product's attributes with the specific months during which those attributes were valid (based on their start and end dates). It filters the results to include months up to December of the current year.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_DATE |
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
| Column Name |
|---|
| PRODUCT_ATTRIBUTE_KEY |
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_DESC |
| START_DATE |
| END_DATE |
| CURRENT_STATUS |
| VERSION |
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
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_FAMILY |
| DRM_COMMON_SERVICE |
| STARTUP_FEE |
| MONTHLY_FEE |
| PRICE_VAT_DESC |
| INCLUDED_MINUTES |
| PRICE_MIN_AFTER_INCLUDED |
| INCLUDED_SMS |
| PRICE_SMS_AFTER_INCLUDED |
| INCLUDED_MMS |
| PRICE_MMS_AFTER_INCLUDED |
| INCLUDED_MB |
| PRICE_MB_AFTER_INCLUDED |
| MAX_MONTHLY_CHARGE_MB |
| BAUD_UPLOAD_MBPS |
| BAUD_DOWNLOAD_MBPS |
| BAUD_REDUCTION_QUOTA_MB |
| TK_PRODUCT_RANK |
| PRODUCT_TYPE_ID |
| PRODUCT_TYPE |
| MD5_COLUMN |


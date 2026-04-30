# PD_WIP

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of product data by combining general product dimensions, specific product attributes, and product type configurations. It details various aspects like product keys, source system identifiers, subscription and product group classifications, product names and descriptions, pricing details (including fees, included services, and data limits), and various DRM (Digital Rights Management) and common product area categorizations. The view also includes flags for product saleability and other technical specifications.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_PRODUCT_ID_2 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_DESC |
| PRODUCT_NAME |
| PRIMARY_PRODUCT_FLAG |
| PRODUCT_BRAND |
| DRM_PRODUCT_CLASS |
| DRM_PRODUCT_NEED |
| PRODUCT_PAYTYPE |
| PRODUCT_START_DATE |
| PRODUCT_END_DATE |
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
| PRODUCT_CATEGORY_ID |
| PRODUCT_CATEGORY_NAME |
| DRM_PRODUCT_BUSINESS_AREA |
| DRM_PRODUCT_BUSINESS_AREA_DET |
| PRODUCT_PORTFOLIO_NAME |
| PRODUCT_FAMILY_NAME |
| PRODUCT_ACCESS_TYPE_NAME |
| PRODUCT_PAYMENT_TYPE_NAME |
| PRODUCT_BINDING_TYPE_NAME |
| PRICE_VAT_DESC |
| VAT_CODE_FLAG |
| TK_INCOME_SERVICE |
| TK_PRODUCT_RANK |
| SB_INCLUDED_DATA |
| FB_BUCKET_SIZE |
| QUARANTINE_LENGTH_MONTHS |
| MAX_NUMBER_OF_GOODIES |

- ← [[CRM_ANALYSE.ADM_PRODUCT_ATTRIBUTE_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| STARTUP_FEE |
| MONTHLY_FEE |
| INCLUDED_MINUTES |
| PRICE_MIN_AFTER_INCLUDED |
| INCLUDED_SMS |
| PRICE_SMS_AFTER_INCLUDED |
| INCLUDED_MMS |
| PRICE_MMS_AFTER_INCLUDED |
| INCLUDED_MB |
| PRICE_DATA_AFTER_INCLUDED |
| PRICE_MB_AFTER_INCLUDED |
| MAX_MONTHLY_CHARGE_MB |
| BAUD_UPLOAD_MBPS |
| BAUD_DOWNLOAD_MBPS |
| BAUD_REDUCTION_QUOTA |
| BAUD_REDUCTION_QUOTA_MB |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| OVERRIDE_SALES_END_DATE |
| PARENT |
| DESCRIPTION |



# VYA_ADM_HIST_PROD_PRICE_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a historical product price dimension view by joining monthly date information with historical product attributes. It filters products based on specific characteristics (brand 'Telenor', category 'Abonnement', reporting type 'Consumerprodukt') and aligns product prices with relevant months, presenting key product and pricing details.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_DATE |
| PERIOD_MONTH_KEY |
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_NAME |
| MONTHLY_FEE |
| START_DATE |
| END_DATE |
| DRM_COMMON_BRAND |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_REPORTING |


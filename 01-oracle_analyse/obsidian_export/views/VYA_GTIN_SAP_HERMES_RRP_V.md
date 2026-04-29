# VYA_GTIN_SAP_HERMES_RRP_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines Recommended Retail Price (RRP) and article information from SAP/Hermes with terminal GTIN properties, primarily for reporting purposes for specific device categories, and includes calculated VAT-inclusive RRPs.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.SAP_TN_WEB_RETL_ARTICLE_INFO]]
| Column Name |
|---|
| DEVICE_EAN |
| EAN |
| CCDW_LOAD_DATE |
| ARTICLE |
| CATEGORY |
| CATEGORY_DESIGNATION |
| SALES_PRICE_EX_VAT |
| VALID_FROM |
| VALID_TO |
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
| Column Name |
|---|
| GTIN |
| MANUFACTURER |
| MODEL_NAME |
| COLOR_NAME |
| TOTAL_SIZE |


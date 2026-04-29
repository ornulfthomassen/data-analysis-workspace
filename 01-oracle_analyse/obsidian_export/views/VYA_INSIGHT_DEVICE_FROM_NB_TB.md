# VYA_INSIGHT_DEVICE_FROM_NB_TB

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts the latest (most recent delivery date) sold handset information for each unique IMEI, specifically from records with a 'NB' file source tag. It performs various data type conversions, formatting, and extracts derived date components (year, month) from original date fields, as well as transforming IMEI into different formats (full, useable prefix) and creating a numerical handset key.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.SOLD_HANDSETS]]
| Column Name |
|---|
| FILE_DATE |
| FILE_SOURCE_TAG |
| ARTICLE_NUMBER |
| ARTICLE_TEXT |
| INVOICE_CREATE_DATE |
| HANDSET_DELIVERED_DATE |
| INVOICE_NUMBER |
| IMEI |
| SALES_DOCUMENT |
| TELENOR_REFERENCE |
| DEALER_ID |
| DEALER_NAME |
| GTIN |


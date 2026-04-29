# VYA_INSIGHT_DEVICE_FROM_NB

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts and processes handset (device) sales data from the 'THIRD_PARTY_SERVICES.SOLD_HANDSETS' table. It filters for records originating from the 'NB' (Netbutikk/online store) channel and, for each unique IMEI, selects only the most recent sales entry based on the handset delivery date. The view standardizes and formats various fields such as IMEI, date components (year, month, full date), and descriptive text fields.

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


# VYA_TELENOR_SPILL_INVOICE

**Schema:** `CCM` | **Type:** `View`

## Description
Loads filtered invoice data for 'Telenor Spill' with a specific traffic type and date range into 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
| Column Name |
|---|
| INVOICE_ID |
| MARKET_AREA_ID |
| INVOICE_DATE |
| INVOICE_LINE_START_DATE |
| INVOICE_LINE_END_DATE |
| GROSS_AMOUNT |
| NET_AMOUNT |
| TRAFFIC_TYPE_ID |
- ← [[CCDW_USAGE.TRAFFIC_TYPE]]
| Column Name |
|---|
| TRAFFIC_TYPE_ID |
| TRAFFIC_TYPE_NAME_3 |


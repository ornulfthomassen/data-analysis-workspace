# NEW_MPP_INVOICE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates recent invoice details, categorizing gross amounts by invoice line type (e.g., one-time, fixed, Telenor Swap, usage) and deriving an invoice status based on specific line types for a defined period and market areas.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
| Column Name |
|---|
| KURT_ID_BILL |
| KURT_ID_SHIPPED |
| KURT_ID_SOLD |
| SUBSCRIPTION_ID |
| INVOICE_DATE |
| DATAVOLUME |
| GROSS_AMOUNT |
| INVOICE_LINE_TYPE_ID |
| source_system_id |
| MARKET_AREA_ID |
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]
| Column Name |
|---|
| INVOICE_LINE_TYPE_KEY |
| INVOICE_LINE_TYPE_DESC |
| INVOICE_LINE_TYPE_NAME |


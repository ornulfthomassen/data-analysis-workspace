# VYAMN_KIM_INVOICE

**Schema:** `CCM` | **Type:** `View`

## Description
This is a test view to get invoice data on an aggregated level to use with other KIM data.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
| Column Name |
|---|
| invoice_id |
| invoice_date |
| gross_amount |
| gl_product_id |
| KURT_ID_SOLD |
| market_area_id |
- ← [[CCDW_INVOICE.INVOICE]]
| Column Name |
|---|
| invoice_due_date |
| invoice_id |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| customer_sk |
| KURT_ID |


# VYAMN_KIM_INVOICE

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates invoice data by invoice ID, date, and customer owner, calculating total gross amount and a specific gross amount for certain GL product IDs. It is designed to provide invoice data at an aggregated level for integration with other KIM (Key Information Management) data.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
- ← [[CCDW_INVOICE.INVOICE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]


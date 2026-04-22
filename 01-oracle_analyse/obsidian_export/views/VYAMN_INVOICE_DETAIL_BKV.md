# VYAMN_INVOICE_DETAIL_BKV

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed invoice transaction data by joining the core invoice details with various dimension tables. It enriches raw invoice data with descriptive attributes related to products, payment methods, invoice line types, and dates. Key transformations include handling NULL values for foreign keys (replacing with -1), casting IDs to character types for surrogate keys, and extracting full date values from date dimension keys, primarily preparing the data for analytical reporting.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.PAYMENT_METHOD_DIM]]
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]


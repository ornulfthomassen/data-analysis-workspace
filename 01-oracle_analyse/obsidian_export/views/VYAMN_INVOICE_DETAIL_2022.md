# VYAMN_INVOICE_DETAIL_2022

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYAMN_INVOICE_DETAIL_2022`, is designed to consolidate and prepare detailed invoice and billing information for analytical purposes. It specifically filters for invoice data from the year 2022 (as indicated by the WHERE clause and view name). The view enriches raw invoice data with details from various dimension tables, including product information, payment methods, invoice line types, and customer mappings. It also includes specific calculated columns (`PERIOD_MONTH_SK`, `MULTI_NODE_COL`) optimized for multi-node analytical queries (e.g., from SAS Viya), and serves as a source for loading 'Order-DATA' into a data warehouse/lake (Mjøsa).

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.PAYMENT_METHOD_DIM]]
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


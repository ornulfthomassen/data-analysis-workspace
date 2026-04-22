# VYAMN_INVOICE_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'VYAMN_INVOICE_DETAIL', consolidates detailed invoice and order data for analytical purposes, specifically for loading into a data warehouse named 'MJØSA'. It combines core invoice line item information with related dimensions such as product details, payment methods, invoice line types, and various date dimensions. It also links to customer mapping data. The view includes calculations for multi-node querying and transforms certain IDs into keys (e.g., SUBSCRIPTION_SK, AGREEMENT_SK, CUSTOMER_SK). It provides granular details like gross/net amounts, duration, data volume, and product attributes for each invoice line.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.PAYMENT_METHOD_DIM]]
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


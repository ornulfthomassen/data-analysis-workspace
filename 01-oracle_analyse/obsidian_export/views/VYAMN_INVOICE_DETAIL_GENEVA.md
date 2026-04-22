# VYAMN_INVOICE_DETAIL_GENEVA

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive, denormalized view of invoice and invoice line item details. It enriches the core invoice data by joining with product, payment method, and various date dimensions, and also incorporates invoice line type descriptions. The view converts date keys into full date values and includes a calculated column ('MULTI_NODE_COL') designed to facilitate parallel processing for multi-node queries, specifically mentioned for SAS Viya, likely for loading into a data warehouse or analytical platform.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.PAYMENT_METHOD_DIM]]
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]


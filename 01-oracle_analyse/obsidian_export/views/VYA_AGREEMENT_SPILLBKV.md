# VYA_AGREEMENT_SPILLBKV

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves detailed information for specific agreements associated with a predefined set of product keys (10896117, 11046082). It combines agreement details with product descriptions and customer mapping information, providing agreement keys, product names, customer identifiers (defaulting to -1 if not found), start/end dates, and various product quantities.

## Data Sources (Inputs)
- ← [[GALAXY.AGREEMENT_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


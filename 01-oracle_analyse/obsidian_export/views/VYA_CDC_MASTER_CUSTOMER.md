# VYA_CDC_MASTER_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated master customer record by joining the core customer data from `CDC.MASTER_CUSTOMER` with customer mapping information from `CLM_ADM.ADM_CUSTOMER_MAPPING`. It selects a wide range of customer attributes, including status, unit details, geographical information, marketing name, classification, region, various metadata fields (registration, change, source, quality, deletion), system presence flags, export status, and sales turnover. The view specifically filters for customers whose mapping status is either 'EKSKUNDE' (former customer) or 'KUNDE' (customer), and assigns a `CUSTOMER_SK` from the mapping table.

## Data Sources (Inputs)
- ← [[CDC.MASTER_CUSTOMER]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]


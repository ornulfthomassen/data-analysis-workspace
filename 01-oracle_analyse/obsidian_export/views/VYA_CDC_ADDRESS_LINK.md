# VYA_CDC_ADDRESS_LINK

**Schema:** `CCM` | **Type:** `View`

## Description
Links address information from a CDC (Change Data Capture) system to customer master data, providing a comprehensive view of customer addresses with associated roles, purposes, and validity periods. It integrates address details with customer mappings based on `MASTER_ID` and `KURT_ID`, filtering for active customer mapping statuses ('EKSKUNDE', 'KUNDE') and ensuring date validity between the address link and customer mapping records.

## Data Sources (Inputs)
- ← [[CDC.ADDRESS_LINK]]
- ← [[CDC.MASTER_CUSTOMER]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]


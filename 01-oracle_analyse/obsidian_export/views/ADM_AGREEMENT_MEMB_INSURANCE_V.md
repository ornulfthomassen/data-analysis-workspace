# ADM_AGREEMENT_MEMB_INSURANCE_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Retrieves the latest insurance-related agreement details (agreement key, product ID, and product name) for each unique device, identified by its IMEI. It specifically filters for agreements classified as 'Forsikring' (insurance) under the 'DEVICE' product group, prioritizing the agreement with the most recent end date for each IMEI.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]


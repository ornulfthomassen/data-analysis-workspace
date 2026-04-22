# ADM_AGREEMENT_MEMB_SWAP_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and retrieves the details of the most recent 'SWAP' (product type) device agreement for each unique IMEI. It filters for agreements that are classified as 'SWAP' products within the 'DEVICE' product group and have a valid IMEI. For each IMEI, it selects the agreement with the latest device agreement end date and provides its IMEI, root agreement key, product agreement ID, and product name.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]


# V_JOE_SWAP_IMEI

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates information related to device IMEIs, their manufacturers, marketing names, and associated customer and subscription details. It specifically focuses on 'swap' scenarios, bringing together various insurance/coverage ('fors') statuses before and after a swap, and links this device/swap data to customer information via a customer mapping table. The 'VOLUME' column indicates each row represents a single record.

## Data Sources (Inputs)
- ← [[ADHOC_BS.AH_2006_SAMMEN]]
- ← [[clm_adm.adm_customer_mapping]]


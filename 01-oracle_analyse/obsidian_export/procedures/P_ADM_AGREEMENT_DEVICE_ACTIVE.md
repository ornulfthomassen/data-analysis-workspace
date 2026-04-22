# P_ADM_AGREEMENT_DEVICE_ACTIVE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_AGREEMENT_DEVICE_ACTIVE` is responsible for recreating and populating a permanent table named `CLM_ADM.ADM_AGREEMENT_DEVICE_ACTIVE`. This table stores filtered and processed device agreement data, likely for analytical or reporting purposes. It selects data from `CCM.VYA_ADM_AGREEMENT_DEVICE_ALL` and enriches it by joining with `CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT` to retrieve owner and user customer IDs. The data is filtered to include only active agreements, excluding internal test/admin agreements, and specific 'SWAP-avtale' and 'orsikring' related entries. After table creation, it grants SELECT privileges on the new table to `CRM_ANALYSE` and logs the operation history.

## Data Sources (Inputs)
- ← [[CCM.VYA_ADM_AGREEMENT_DEVICE_ALL]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_AGREEMENT_DEVICE_ACTIVE]]


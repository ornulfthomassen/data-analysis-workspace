# P_ADM_AGREEMENT_DEVICE_TRANSFR

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure identifies and tracks device transfer sequences (e.g., swaps) by populating and subsequently updating the `ADM_AGREEMENT_DEVICE_TRANSFER` table. It initially inserts new records into `ADM_AGREEMENT_DEVICE_TRANSFER` from `ADM_AGREEMENT_DEVICE_ALL`, filtering for active agreements with specific ranging and end date conditions, while excluding already processed transfers. It then iteratively updates these records within `ADM_AGREEMENT_DEVICE_TRANSFER` to establish detailed linkage information, such as matched dates, criteria, and the timing (days between) of successive agreements for the same device (IMEI), distinguishing between 'first' and 'next' agreements in a transfer chain. The procedure also includes logging of its operations and error handling.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_TRANSFER]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]

## Target Tables (Outputs)
- → [[ADM_AGREEMENT_DEVICE_TRANSFER]]


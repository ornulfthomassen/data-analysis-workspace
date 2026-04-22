# P_ADM_SWAP_AGREEMENT_TRANSFERE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure is designed to manage and enrich device swap agreement transfer data. It first identifies new swap agreement records by comparing current counts in `ADM_STOCK_AGREEMENT_DEVICE_ALL` with existing records in `ADM_SWAP_AGREEMENT_TRANSFERE`. It then inserts these new records into `ADM_SWAP_AGREEMENT_TRANSFERE`, initializing several 'matched' and 'first/next' agreement fields to NULL. Subsequently, it updates records within `ADM_SWAP_AGREEMENT_TRANSFERE` to populate these previously NULL fields, linking sequential agreements for the same device (identified by IMEI) and calculating metrics like days between agreements, as well as identifying specific match criteria for the transfer.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
- ← [[CLM_ADM.ADM_SWAP_AGREEMENT_TRANSFERE]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_SWAP_AGREEMENT_TRANSFERE]]


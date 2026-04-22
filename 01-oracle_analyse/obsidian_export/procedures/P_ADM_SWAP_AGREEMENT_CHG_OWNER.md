# P_ADM_SWAP_AGREEMENT_CHG_OWNER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_SWAP_AGREEMENT_CHG_OWNER` identifies and matches pairs of 'SWAP' product agreements that share the same 'root agreement key'. It applies two different matching criteria (C1: O.END_DATE = N.REG_DATE; C2: O.END_DATE > N.REG_DATE) to find these pairs. For each identified matching pair, it updates the `ADM_SWAP_AGREEMENT_CHG_OWNER` table, setting the `MATCED_DATE`, `MATCH_CRITERIA`, `MATCHED_PRODUKT_AGREEMENT_ID`, and `DAYS_BETWEEN_AGREEMENTS` fields. The procedure enforces a strict rule of updating exactly one row per matching item, raising exceptions if fewer or more than one row are affected.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SWAP_AGREEMENT_CHG_OWNER]]
- ← [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[ADM_SWAP_AGREEMENT_CHG_OWNER]]


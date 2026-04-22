# P_ADM_SWAP_AGREEMENT_SWAPPED

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure initializes and subsequently updates the ADM_SWAP_AGREEMENT_SWAPPED table. It first inserts new 'swap' agreement records, identified by specific status and ranking, into this table. Following this, it iteratively applies a series of 17 different matching rules (defined by cursors C1-C17). For each rule, it identifies previously unmatched swap agreements within the ADM_SWAP_AGREEMENT_SWAPPED table and updates their records with match details, including the matched product agreement ID, the specific matching criteria used (e.g., 'Same root agreement, 2 SWAP agreements, O.END_DATE = N.REG_DATE'), the matching date, and the number of days between the agreements. The overall purpose is to identify and link related 'swap' agreements based on a complex set of business rules.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]
- ← [[CLM_ADM.ADM_SWAP_AGREEMENT_SWAPPED]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]

## Target Tables (Outputs)
- → [[ADM_SWAP_AGREEMENT_SWAPPED]]


# P_ADM_AGREEMENT_DEVICE_SWAPPED

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure identifies and matches 'device swap' agreements. It first populates the `ADM_AGREEMENT_DEVICE_SWAPPED` table with new, initially unmatched agreements based on recent product agreement end dates. Subsequently, it iteratively updates these unmatched agreements by applying a series of progressively more specific matching rules (defined by cursors C1 through C17). Each rule attempts to find a corresponding 'new' device agreement for an 'old' one, based on criteria like root agreement key, main number, device manufacturer, operating system, and time differences between agreement end and registration dates. Once a match is found, the `ADM_AGREEMENT_DEVICE_SWAPPED` entry is updated with the `MATCHED_DATE`, `MATCH_CRITERIA`, `MATCHED_PRODUKT_AGREEMENT_ID`, and `DAYS_BETWEEN_AGREEMENTS`.

## Data Sources (Inputs)
- ← [[ADM_AGREEMENT_DEVICE_SWAPPED]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]

## Target Tables (Outputs)
- → [[ADM_AGREEMENT_DEVICE_SWAPPED]]


# ADM_PREV_ORIG_SUBS_MASTER2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Traces back the lineage of a given subscription ID (P_SUBS_ID) within the ADM_MOB_SUBSCR_MASTER_RAW2 table. It recursively follows the chain of 'PREV_SUBSCRIPTION_ID' and 'ORIG_SUBSCRIPTION_ID' links to identify the ultimate original or 'root' subscription ID in its hierarchy or historical chain. The function returns the initial P_SUBS_ID if no previous link is found or if the found link points back to the current ID, effectively stopping the recursion.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCR_MASTER_RAW2]]


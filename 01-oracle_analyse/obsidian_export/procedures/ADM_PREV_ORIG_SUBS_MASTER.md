# ADM_PREV_ORIG_SUBS_MASTER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces subscription IDs within the ADM_MOB_SUBSCRIPTION_CORE table by following `PREV_SUBSCRIPTION_ID` and `ORIG_SUBSCRIPTION_ID` links. The function aims to identify and return the ultimate 'original' or 'master' subscription ID in a hierarchical chain, starting from an input subscription ID (P_SUBS_ID). If no related record is found, it returns the input P_SUBS_ID.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]


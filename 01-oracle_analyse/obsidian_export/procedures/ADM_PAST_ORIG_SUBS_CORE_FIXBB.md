# ADM_PAST_ORIG_SUBS_CORE_FIXBB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces subscription lineage within the 'ADM_SUBSCRIPTION_CORE_FIXBB' table to find and return a specific related subscription ID (original, past, or previous) based on complex hierarchical rules derived from 'PAST_SUBSCRIPTION_ID', 'ORIG_SUBSCRIPTION_ID', and 'PREV_SUBSCRIPTION_ID' fields, starting from a given input subscription ID (P_SUBS_ID).

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIXBB]]


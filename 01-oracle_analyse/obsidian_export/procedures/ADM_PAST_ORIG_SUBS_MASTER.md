# ADM_PAST_ORIG_SUBS_MASTER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL function, despite some syntax irregularities in the provided script, is designed to recursively trace and return a 'master' or 'original' subscription ID. Given an initial `P_SUBS_ID`, it queries the `ADM_MOB_SUBSCRIPTION_CORE` table to identify related subscription IDs (original, previous, or past) based on a complex set of conditions. If a definitive 'master' ID is found (indicated by a derived internal status), that ID is returned. Otherwise, the function recursively calls itself with a newly identified related subscription ID, continuing the search down the subscription lineage until a master is found or no further related data exists.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]


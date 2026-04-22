# ADM_PAST_ORIG_SUBS_CORE_FIX_T

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The script defines a recursive Oracle PL/SQL function named ADM_PAST_ORIG_SUBS_CORE_FIX_T. Its purpose is to trace and identify a 'core' or 'original' subscription ID starting from a given P_SUBS_ID. It navigates through the subscription lineage using columns like PAST_SUBSCRIPTION_ID, ORIG_SUBSCRIPTION_ID, and PREV_SUBSCRIPTION_ID within the ADM_SUBSCRIPTION_CORE_FIX_T table. The function employs complex conditional logic (CASE statements) to determine the next subscription ID to investigate or to identify a final 'original' ID based on specific criteria. If the search path leads to no matching data, the function returns NULL. The function repeatedly calls itself with a new V_SUBS_ID until an 'OK' condition is met for V_CASE, at which point it returns the determined V_SUBS_ID.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIX_T]]


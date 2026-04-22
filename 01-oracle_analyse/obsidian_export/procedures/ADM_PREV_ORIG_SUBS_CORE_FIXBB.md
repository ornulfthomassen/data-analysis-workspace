# ADM_PREV_ORIG_SUBS_CORE_FIXBB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The function `ADM_PREV_ORIG_SUBS_CORE_FIXBB` aims to resolve a given subscription ID (`P_SUBS_ID`) to its ultimate original or initial subscription ID within a chain. It does this by recursively tracing back through related subscriptions in the `ADM_SUBSCRIPTION_CORE_FIXBB` table. For each step, it attempts to find an 'original' ID, prioritizing `SUBS.ORIG_SUBSCRIPTION_ID`, then `SUBS0.ORIG_SUBSCRIPTION_ID`, and finally `SUBS0.PREV_SUBSCRIPTION_ID`. The recursion continues until an ID is found that doesn't lead to a new link in the chain or if the input ID itself is the 'original' one. If the initial `P_SUBS_ID` is not found in the table, it returns the `P_SUBS_ID` itself.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIXBB]]


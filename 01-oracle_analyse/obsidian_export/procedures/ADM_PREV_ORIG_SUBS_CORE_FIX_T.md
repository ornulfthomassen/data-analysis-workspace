# ADM_PREV_ORIG_SUBS_CORE_FIX_T

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces the lineage of a subscription ID within the `ADM_SUBSCRIPTION_CORE_FIX_T` table. It aims to find the ultimate original or earliest preceding subscription ID by following `ORIG_SUBSCRIPTION_ID` and `PREV_SUBSCRIPTION_ID` links. The function uses self-joins to navigate through subscription history until it reaches a point where no further previous subscription is found or the ID stabilizes.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIX_T]]


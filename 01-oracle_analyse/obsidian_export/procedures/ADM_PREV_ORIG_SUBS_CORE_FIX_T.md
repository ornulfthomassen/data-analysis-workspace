# ADM_PREV_ORIG_SUBS_CORE_FIX_T

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces the lineage of a given subscription ID (`P_SUBS_ID`) within the `ADM_SUBSCRIPTION_CORE_FIX_T` table to find its ultimate original or preceding subscription ID. It prioritizes `ORIG_SUBSCRIPTION_ID` from the current or immediately preceding record, falling back to the `PREV_SUBSCRIPTION_ID` of the preceding record if `ORIG_SUBSCRIPTION_ID` is not found. The recursion continues until an ultimate predecessor is identified (where the predecessor's ID points back to itself or no further predecessors are found).

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIX_T]]
| Column Name |
|---|
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| SUBSCRIPTION_ID |


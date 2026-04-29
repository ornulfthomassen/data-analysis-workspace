# ADM_PAST_ORIG_SUBS_CORE_FIX_T

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This recursive PL/SQL function traces the lineage of a given subscription ID within the `ADM_SUBSCRIPTION_CORE_FIX_T` table. It identifies the ultimate original or designated past subscription ID by evaluating complex conditions based on `SUBSCRIPTION_ID`, `ORIG_SUBSCRIPTION_ID`, `PREV_SUBSCRIPTION_ID`, and `PAST_SUBSCRIPTION_ID`. The function recursively calls itself until a definitive 'OK' state is reached, returning the resolved subscription ID.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIX_T]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| PAST_SUBSCRIPTION_ID |


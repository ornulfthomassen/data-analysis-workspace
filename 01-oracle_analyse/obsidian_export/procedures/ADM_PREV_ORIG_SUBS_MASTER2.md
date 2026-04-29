# ADM_PREV_ORIG_SUBS_MASTER2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Traces the lineage of a subscription ID within the `ADM_MOB_SUBSCR_MASTER_RAW2` table to find its ultimate original or previous subscription ID through a recursive lookup process. It prioritizes the `ORIG_SUBSCRIPTION_ID` if available, otherwise it uses `PREV_SUBSCRIPTION_ID` to follow the chain.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCR_MASTER_RAW2]]
| Column Name |
|---|
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| SUBSCRIPTION_ID |


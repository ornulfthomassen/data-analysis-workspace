# ADM_PAST_ORIG_SUBS_MASTER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle function, ADM_PAST_ORIG_SUBS_MASTER, traces the lineage of a subscription to identify its ultimate 'original' or 'master' subscription ID. It uses a recursive approach, querying the ADM_MOB_SUBSCRIPTION_CORE table to determine the relevant subscription based on various lineage columns (PAST_SUBSCRIPTION_ID, PREV_SUBSCRIPTION_ID, ORIG_SUBSCRIPTION_ID).

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| PAST_SUBSCRIPTION_ID |


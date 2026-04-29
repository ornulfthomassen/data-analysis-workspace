# WMP_PAST_ORIG_SUBS_MASTER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces a subscription's lineage within the `WMP_MOB_SUBSCRIPTION_CORE` table to determine and return its ultimate 'master' or 'original' subscription ID, based on various subscription relationship fields (ORIG_SUBSCRIPTION_ID, PAST_SUBSCRIPTION_ID, PREV_SUBSCRIPTION_ID).

## Data Sources (Inputs)
- ← [[WMP_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PAST_SUBSCRIPTION_ID |
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |


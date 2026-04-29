# ADM_PAST_ORIG_SUBS_MASTER2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces subscription lineage within ADM_MOB_SUBSCR_MASTER_RAW2 to find an original or primary subscription ID based on past and previous subscription links. It determines the next subscription ID to evaluate or the final 'original' ID based on a complex set of conditions involving 'ORIG_SUBSCRIPTION_ID', 'PREV_SUBSCRIPTION_ID', and 'PAST_SUBSCRIPTION_ID'.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCR_MASTER_RAW2]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| PAST_SUBSCRIPTION_ID |


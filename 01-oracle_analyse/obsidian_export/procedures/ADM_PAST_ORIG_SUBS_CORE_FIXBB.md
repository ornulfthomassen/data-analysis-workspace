# ADM_PAST_ORIG_SUBS_CORE_FIXBB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively resolves the original or core subscription ID by tracing historical links (original, previous, and past subscription IDs) within the `ADM_SUBSCRIPTION_CORE_FIXBB` table, returning the final resolved ID or NULL if not found. The function traverses the subscription lineage until a stable 'original' or 'past' subscription is identified based on complex conditional logic.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIXBB]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| PAST_SUBSCRIPTION_ID |


# ADM_PREV_ORIG_SUBS_CORE_FIXBB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively resolves the ultimate original subscription ID by traversing `PREV_SUBSCRIPTION_ID` links within the `ADM_SUBSCRIPTION_CORE_FIXBB` table, favoring direct `ORIG_SUBSCRIPTION_ID` values. It returns the input subscription ID if no further lineage is found or if the derived ID matches the input.

## Data Sources (Inputs)
- ← [[ADM_SUBSCRIPTION_CORE_FIXBB]]
| Column Name |
|---|
| ORIG_SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| SUBSCRIPTION_ID |


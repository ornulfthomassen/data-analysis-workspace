# ADM_PREV_ORIG_SUBS_MASTER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces back subscription IDs (original or previous) within the ADM_MOB_SUBSCRIPTION_CORE table to find the ultimate master or original subscription ID in a chain. It starts with a given subscription ID and follows the `PREV_SUBSCRIPTION_ID` link, or retrieves the `ORIG_SUBSCRIPTION_ID`, until it reaches the top of the chain.

## Data Sources (Inputs)
- ← [[ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PREV_SUBSCRIPTION_ID |
| ORIG_SUBSCRIPTION_ID |


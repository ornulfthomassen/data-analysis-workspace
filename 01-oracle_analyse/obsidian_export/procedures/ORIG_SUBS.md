# ORIG_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This PL/SQL function recursively traces the history of a given subscription ID (`SUBS_ID`) within the `ADM_MOBIL_SUBSCR_HIST_RAW` table. It identifies the immediate preceding subscription, if any, by matching `MAIN_NUMBER` and chronological date ranges (`START_DATE`, `END_DATE`, `ORIGINAL_START_DATE`). The function continues this process until it reaches the earliest linked subscription ID in the chain, which it then returns. If no preceding subscription is found (i.e., no data matches the criteria), or if the initial subscription ID does not have a historical link, the original `SUBS_ID` is returned.

## Data Sources (Inputs)
- ← [[ADM_MOBIL_SUBSCR_HIST_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| ORIGINAL_START_DATE |


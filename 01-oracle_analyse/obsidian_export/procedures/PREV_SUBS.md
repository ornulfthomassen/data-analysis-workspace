# PREV_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This function retrieves a 'previous' subscription ID for a given input subscription ID from the ADM_MOBIL_SUBSCR_HIST_RAW table. It first attempts to find a subscription (aliased as SUBS0) that ended exactly when the input subscription (SUBS) started, or failing that, a subscription (aliased as SUBS1) that ended one day before the input subscription started. If neither is found, or if the initial input subscription ID is not found in the table, it returns the original input subscription ID. The logic ensures that the 'previous' subscriptions (SUBS0, SUBS1) have valid start/end date ranges and are linked by their main number.

## Data Sources (Inputs)
- ← [[ADM_MOBIL_SUBSCR_HIST_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| ORIGINAL_START_DATE |


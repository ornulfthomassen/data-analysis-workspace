# ADS_PREV_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Retrieves a 'previous' subscription ID from the `ADS_MOBIL_SUBSCR_HIST_RAW` table based on a given subscription ID. It identifies previous records using `MAIN_NUMBER` and specific date relationships (`START_DATE`, `END_DATE`, `ORIGINAL_START_DATE`). The logic prioritizes records ending exactly when the current subscription starts, then records ending one day prior. If no matching 'previous' subscription is found, the original `SUBS_ID` is returned.

## Data Sources (Inputs)
- ← [[ADS_MOBIL_SUBSCR_HIST_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| ORIGINAL_START_DATE |


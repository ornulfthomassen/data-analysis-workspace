# ODS_ADS_ORIG_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle function, ODS_ADS_ORIG_SUBS, recursively traces back subscription history for a given SUBS_ID to find its ultimate original (earliest linked) subscription ID. It identifies preceding subscriptions based on matching MAIN_NUMBER and contiguous or near-contiguous date ranges (START_DATE, END_DATE, ORIGINAL_START_DATE) within the ADS_MOBIL_SUBSCR_HIST_RAW table. If a direct predecessor is found, it recursively calls itself with the predecessor's ID until no further predecessors are found, or the original SUBS_ID itself is determined to be the 'origin'.

## Data Sources (Inputs)
- ← [[ADS_MOBIL_SUBSCR_HIST_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| ORIGINAL_START_DATE |


# ADS_ORIG_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `ADS_ORIG_SUBS` function recursively traces back and identifies the earliest (original) subscription ID in a historical chain of linked subscriptions. It takes a `SUBS_ID` as input, queries the `ADS_MOBIL_SUBSCR_HIST_RAW` table to find preceding subscription records based on a shared `MAIN_NUMBER` and specific date-linking conditions (`START_DATE`, `END_DATE`, `ORIGINAL_START_DATE`). If an earlier subscription ID is found, the function calls itself recursively with that ID until no further preceding record can be identified, at which point the truly 'original' subscription ID is returned. If no related historical data is found, the input `SUBS_ID` is returned as the original.

## Data Sources (Inputs)
- ← [[ADS_MOBIL_SUBSCR_HIST_RAW]]


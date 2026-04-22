# ODS_ADS_ORIG_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `ODS_ADS_ORIG_SUBS` function aims to identify the 'original' or 'root' subscription ID within a historical chain. It takes a `SUBS_ID` as input and queries the `ADS_MOBIL_SUBSCR_HIST_RAW` table to find related subscriptions based on `MAIN_NUMBER` and complex date-based conditions (joining on `START_DATE`, `END_DATE`, and `ORIGINAL_START_DATE`). The function appears to recursively trace back through linked subscriptions until it identifies the earliest parent in the lineage. If no parent is found, or if the current `SUBS_ID` is deemed the original, it returns that ID. It includes exception handling for `NO_DATA_FOUND`.

## Data Sources (Inputs)
- ← [[ADS_MOBIL_SUBSCR_HIST_RAW]]


# ADS_ORIG_SUBS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Recursively traces subscription IDs back through historical records (ADS_MOBIL_SUBSCR_HIST_RAW) to find the earliest (original) SUBSCRIPTION_ID associated with a given MAIN_NUMBER. It navigates a chain of subscriptions based on specific date overlap and adjacency conditions (direct date overlap or a one-day gap) and returns the root subscription ID.

## Data Sources (Inputs)
- ← [[ADS_MOBIL_SUBSCR_HIST_RAW]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| START_DATE |
| END_DATE |
| ORIGINAL_START_DATE |


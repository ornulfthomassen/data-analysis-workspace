# KIM_VA_HIST_DELTA_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the maximum 'target_key' from the 'CI_CUST_HISTORY_LOG' table, considering only historical records with a 'start_time' before the current day. This is likely used to identify the latest processed key from past data for delta processing or historical analysis.

## Data Sources (Inputs)
- ← [[clm_cdm.CI_CUST_HISTORY_LOG]]
| Column Name |
|---|
| target_key |
| start_time |


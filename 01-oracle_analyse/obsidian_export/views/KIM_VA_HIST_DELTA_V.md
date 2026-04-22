# KIM_VA_HIST_DELTA_V

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the maximum `target_key` from the `CI_CUST_HISTORY_LOG` table, specifically considering only those records whose `start_time` (truncated to date) is earlier than the current day. This view likely serves to identify a high watermark or a delta marker for historical data processing, excluding any activity from the current day.

## Data Sources (Inputs)
- ← [[clm_cdm.CI_CUST_HISTORY_LOG]]


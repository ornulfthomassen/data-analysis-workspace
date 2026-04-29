# EXAMPLE_VIEW_WITH_PROC

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`EXAMPLE_VIEW_WITH_PROC`) demonstrates the use of a `WITH` clause to embed a procedure (`WP_CREATE_TMP_DEVICE_DIM`) and a function (`f_test`). The procedure dynamically creates a temporary table (`TABLE_FROM_PROC_IN_WITH`) by selecting `DEVICE_KEY` and `SOURCE_DEVICE_ID` from `GALAXY.DEVICE_DIM`, after potentially waiting for data freshness from `V_WAIT_FOR_DATA`. The view then selects all columns from this dynamically created temporary table, exposing them as `DEVICE_KEY` and `IMEI_USE`.

## Data Sources (Inputs)
- ← [[V_WAIT_FOR_DATA]]
| Column Name |
|---|
| DATA_IS_FRESH |
- ← [[GALAXY.DEVICE_DIM]]
| Column Name |
|---|
| DEVICE_KEY |
| SOURCE_DEVICE_ID |
- ← [[CCM.TABLE_FROM_PROC_IN_WITH]]
| Column Name |
|---|
| DEVICE_KEY |
| IMEI_USE |


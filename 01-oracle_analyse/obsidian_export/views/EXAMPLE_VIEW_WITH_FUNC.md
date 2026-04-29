# EXAMPLE_VIEW_WITH_FUNC

**Schema:** `CCM` | **Type:** `View`

## Description
This view dynamically creates and populates a temporary table (`CCM.TABLE_FROM_PROC_IN_WITH`) from `GALAXY.DEVICE_DIM` after an initial wait period dependent on the freshness status from `V_WAIT_FOR_DATA`. It then exposes `DEVICE_KEY` and `IMEI_USE` from this dynamically generated table, effectively providing a processed subset of device information.

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


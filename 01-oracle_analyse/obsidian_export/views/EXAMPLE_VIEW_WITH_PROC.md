# EXAMPLE_VIEW_WITH_PROC

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a dynamic snapshot of the first 5 records (based on ROWNUM) from the `GALAXY.DEVICE_DIM` table, exposing `DEVICE_KEY` and `IMEI_USE`. Every time the view is queried, it executes a PL/SQL procedure (`WP_CREATE_TMP_DEVICE_DIM`) that first waits for data to be fresh (by checking `V_WAIT_FOR_DATA`), then drops and recreates a 'temporary' table named `TABLE_FROM_PROC_IN_WITH` based on `GALAXY.DEVICE_DIM`. Finally, the view selects from this newly generated table. This design performs DDL operations on a persistent table upon each view access.

## Data Sources (Inputs)
- ← [[V_WAIT_FOR_DATA]]
- ← [[GALAXY.DEVICE_DIM]]
- ← [[CCM.TABLE_FROM_PROC_IN_WITH]]


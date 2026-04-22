# EXAMPLE_VIEW_WITH_FUNC

**Schema:** `CCM` | **Type:** `View`

## Description
The view `EXAMPLE_VIEW_WITH_FUNC` provides `DEVICE_KEY` and `IMEI_USE` (derived from `SOURCE_DEVICE_ID`) for the first 5 records. Its unique design involves a pre-execution phase triggered by a function `f_test` in its `WHERE` clause. This function first waits for data freshness, indicated by the `DATA_IS_FRESH` column in `V_WAIT_FOR_DATA`, for a maximum of 30 seconds. Upon successful data freshness, it dynamically creates (or drops and recreates) a temporary table named `CCM.TABLE_FROM_PROC_IN_WITH` by selecting `DEVICE_KEY` and casting `SOURCE_DEVICE_ID` from `GALAXY.DEVICE_DIM`. Finally, the view selects all columns from this dynamically generated `CCM.TABLE_FROM_PROC_IN_WITH` table.

## Data Sources (Inputs)
- ← [[V_WAIT_FOR_DATA]]
- ← [[GALAXY.DEVICE_DIM]]


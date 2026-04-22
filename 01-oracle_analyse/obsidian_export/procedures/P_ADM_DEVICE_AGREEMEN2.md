# P_ADM_DEVICE_AGREEMEN2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Loads or refreshes monthly device agreement data into a specific partition of the `ADM_DEVICE_AGREEMEN2` table. It does this by first creating a temporary staging table with the new data for the target month, then performing a partition exchange to replace the existing partition (or create a new one) in `ADM_DEVICE_AGREEMEN2` with the data from the temporary table. Finally, it gathers statistics for the updated partition.

## Data Sources (Inputs)
- ← [[ADM_DEVICE_AGREEMENT]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]

## Target Tables (Outputs)
- → [[TMP_ADM_DEVICE_AGREEMENT]]
- → [[ADM_DEVICE_AGREEMEN2]]


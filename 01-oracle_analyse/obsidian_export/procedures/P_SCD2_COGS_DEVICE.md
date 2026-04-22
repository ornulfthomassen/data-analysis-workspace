# P_SCD2_COGS_DEVICE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The provided script snippet is incomplete, lacking the main BEGIN...END block. However, based on the procedure name 'P_SCD2_COGS_DEVICE' and the declared variable names (e.g., 'SCD2_COGS_DEVICE_CURR', 'TMP_SCD2_COGS_DEVICE_CURR_REC'), its intended purpose is to implement and manage Slowly Changing Dimension Type 2 (SCD2) for Cost of Goods Sold (COGS) data specifically for devices. This typically involves identifying changes in source data, marking old records as inactive, and inserting new records with updated effective dates to maintain a complete history of changes. The 'P_NUMBER_OF_DAYS' parameter suggests it likely processes data incrementally for a specified period.

## Target Tables (Outputs)
- → [[SCD2_COGS_DEVICE_CURR]]
- → [[TMP_COGS_DEVICE_CURR]]
- → [[TMP_SCD2_COGS_DEVICE_CURR_REC]]
- → [[TMP_SCD2_COGS_DEVICE_PAST_REC]]


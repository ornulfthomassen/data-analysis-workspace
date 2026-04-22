# STOCK_MOBILE_HISTORY_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `STOCK_MOBILE_HISTORY_DAY` procedure creates daily snapshots or copies of existing stock mobile history tables. It first calls an external procedure, `CLM_ADM.STOCK_MOBILE_HISTORY`. Subsequently, for two pairs of tables (detailed and aggregated history), it performs the following steps: checks if the 'daily' target table exists, drops it if found, creates a new 'daily' table by copying all data from its respective source table, grants SELECT privileges to `CRM_ANALYSE`, gathers table statistics, and logs the process status.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]


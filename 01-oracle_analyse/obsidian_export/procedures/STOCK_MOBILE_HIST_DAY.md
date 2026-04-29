# STOCK_MOBILE_HIST_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure creates daily snapshots of historical stock data. It first invokes another procedure (CLM_ADM.STOCK_MOBILE_HIST) to presumably refresh source historical tables. Then, for two sets of historical data (detailed and aggregated), it performs a drop-and-recreate operation, copying all data from the source historical tables (STOCK_MOBILE_HIST_DET and STOCK_MOBILE_HIST_AGG) into their respective daily snapshot tables (STOCK_MOBILE_HIST_DAY_DET and STOCK_MOBILE_HIST_DAY_AGG). Finally, it grants SELECT privileges on the newly created daily tables and gathers statistics for performance optimization. It also logs its progress using a separate history logging procedure.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CLM_ADM.STOCK_MOBILE_HIST_DET]]
- ← [[CLM_ADM.STOCK_MOBILE_HIST_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HIST_DAY_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HIST_DAY_AGG]]


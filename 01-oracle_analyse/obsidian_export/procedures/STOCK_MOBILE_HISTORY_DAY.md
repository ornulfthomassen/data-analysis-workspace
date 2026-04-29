# STOCK_MOBILE_HISTORY_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure first executes an external procedure 'CLM_ADM.STOCK_MOBILE_HISTORY'. Then, for two pairs of tables (STOCK_MOBILE_HISTORY_DET / STOCK_MOBILE_HISTORY_DAY_DET and STOCK_MOBILE_HISTORY_AGG / STOCK_MOBILE_HISTORY_DAY_AGG), it performs a 'housekeeping' step by dropping the target '_DAY' table if it exists. Subsequently, it creates these '_DAY' tables as full copies (snapshots) of their respective source tables ('STOCK_MOBILE_HISTORY_DET' to 'STOCK_MOBILE_HISTORY_DAY_DET' and 'STOCK_MOBILE_HISTORY_AGG' to 'STOCK_MOBILE_HISTORY_DAY_AGG'). It also grants SELECT privileges and gathers table statistics for the newly created tables. The procedure logs its load history via calls to 'CRM_ANALYSE.P_ADM_LOAD_HISTORY'.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_MOBILE_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_DET]]
- → [[CLM_ADM.STOCK_MOBILE_HISTORY_DAY_AGG]]


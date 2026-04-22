# STOCK_FTV_HISTORY_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure, `STOCK_FTV_HISTORY_DAY`, is responsible for creating daily snapshots of 'stock FTV history' data. It first calls another procedure, `CLM_ADM.STOCK_FTV_HISTORY`, likely to update the base data. Subsequently, it processes two main sets of data: detailed (`_DET`) and aggregated (`_AGG`). For each set, it checks if a corresponding daily snapshot table (e.g., `STOCK_FTV_HISTORY_DAY_DET`) already exists. If so, it drops the existing table. Then, it creates a new daily snapshot table by copying all data from its respective source table (e.g., `STOCK_FTV_HISTORY_DET`). Finally, it grants `SELECT` privileges on the newly created snapshot tables to `CRM_ANALYSE` and gathers statistics.

## Data Sources (Inputs)
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_AGG]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[STOCK_FTV_HISTORY_DAY_DET]]
- → [[STOCK_FTV_HISTORY_DAY_AGG]]


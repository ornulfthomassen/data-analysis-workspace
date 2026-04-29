# STOCK_FTV_HISTORY_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure captures the state of two 'history' tables (detail and aggregated) from the previous day. It first ensures the source history tables are updated by calling another procedure (`CLM_ADM.STOCK_FTV_HISTORY`). Then, for both detail and aggregated data, it drops the existing 'daily history' table if it exists, creates a new 'daily history' table as a full copy of its corresponding 'history' source table, grants SELECT privileges on the new table, gathers statistics, and logs the process status to a load history table.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CLM_ADM.STOCK_FTV_HISTORY_DET]]
- ← [[CLM_ADM.STOCK_FTV_HISTORY_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.STOCK_FTV_HISTORY_DAY_DET]]
- → [[CLM_ADM.STOCK_FTV_HISTORY_DAY_AGG]]
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| LOAD_DATE_KEY |
| STATUS |
| MESSAGE |


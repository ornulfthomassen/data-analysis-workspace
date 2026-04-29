# ADM50_SCORING_TABLES

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure manages and refreshes four 'scoring' tables: ADM_SCORING_TABLE_CUST, ADM_SCORING_TABLE_MPP, ADM_SCORING_TABLE_MPR, and ADM_SCORING_TABLE_MBB. It can process all tables or a specific one based on input parameters. For each target table, it creates a new version (or 'NY' staging table) by selecting all data from a corresponding source view, filtered by a specified or default previous month's 'PERIOD_MONTH_KEY'. It then implements a 'hot-swap' mechanism: the existing main table is renamed to a backup ('BK' table), the newly created staging table ('NY' table) is renamed to become the active main table, and finally, the backup table is dropped. Unique indexes are also created and renamed accordingly. If the main table does not exist initially, it is created directly without a backup process.

## Data Sources (Inputs)
- ← [[V_SCORING_TABLE_CUST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[V_SCORING_TABLE_MPP]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[V_SCORING_TABLE_MPR]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[V_SCORING_TABLE_MBB]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[ADM_SCORING_TABLE_CUST]]
- → [[ADM_SCORING_TABLE_CUSTNY]]
- → [[ADM_SCORING_TABLE_CUSTBK]]
- → [[ADM_SCORING_TABLE_MPP]]
- → [[ADM_SCORING_TABLE_MPP_NY]]
- → [[ADM_SCORING_TABLE_MPP_BK]]
- → [[ADM_SCORING_TABLE_MPR]]
- → [[ADM_SCORING_TABLE_MPR_NY]]
- → [[ADM_SCORING_TABLE_MPR_BK]]
- → [[ADM_SCORING_TABLE_MBB]]
- → [[ADM_SCORING_TABLE_MBB_NY]]
- → [[ADM_SCORING_TABLE_MBB_BK]]


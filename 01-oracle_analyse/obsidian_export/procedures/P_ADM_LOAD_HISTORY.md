# P_ADM_LOAD_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Logs and monitors ETL job execution for specified tables. It verifies table existence, checks for row count changes (current vs. prior period, and current vs. historical maximum), calculates percentage differences, and assigns a job status (OK, WARNING, ERROR). All execution details, including status, row counts, and timing, are recorded in an administrative history table.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[USER_TAB_COLS]]
| Column Name |
|---|
| TABLE_NAME |
| COLUMN_NAME |
- ← [[DUAL]]
- ← [[CLM_ADM.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| ROWS_AFTER |
| LOAD_ID |
| ETL_TABLE |
| PERIOD |
| JOBSTATUS |
| SESSIONID |
| START_DTTM |
- ← [[Dynamic_P_ETL_TABLE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |
| LOAD_FREQUENCY |
| JOB_USER |
| JOBNAME |
| JOBSTATUS |
| SID |
| SESSIONID |
| ETL_TABLE |
| PERIOD |
| ROWS_BEFORE |
| ROWS_AFTER |
| START_DTTM |
| END_DTTM |
| DURATION |
| START_LINE_NUMBER |
| END_LINE_NUMBER |
| STATUS_MESSAGE |


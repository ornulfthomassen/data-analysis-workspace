# TMP_P_ADM_LOAD_HISTORY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure logs and monitors the status of ETL jobs for a specified table (`P_ETL_TABLE`) and period (`P_PERIOD`). It records row counts before and after processing, calculates row count differences (compared to the prior period and maximum historical count), and logs job status (RUNNING, ENDED OK, ERROR, WARNING) along with associated messages into an administrative load history table. It handles cases where the ETL table may or may not have a `PERIOD_MONTH_KEY` column for filtering.

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
- ← [[<DYNAMICALLY DETERMINED P_ETL_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |
| ETL_TABLE |
| PERIOD |
| JOBSTATUS |
| SESSIONID |
| ROWS_AFTER |
| START_DTTM |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |
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


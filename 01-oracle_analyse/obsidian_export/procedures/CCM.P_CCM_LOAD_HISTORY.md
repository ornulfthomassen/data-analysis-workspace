# P_CCM_LOAD_HISTORY

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Records job execution history, including caller details, status, timestamps, and PowerCenter-specific information, into the permanent CCM_LOAD_HISTORY table.

## Target Tables (Outputs)
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |
| JOB_USER |
| JOBNAME |
| JOBSTATUS |
| SID |
| SESSIONID |
| ETL_TABLE |
| ROWS_BEFORE |
| ROWS_AFTER |
| START_DTTM |
| END_DTTM |
| DURATION |
| START_LINE_NUMBER |
| END_LINE_NUMBER |
| STATUS_MESSAGE |
| WORKFLOW_NAME |
| SESSION_NAME |



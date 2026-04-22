# P_ADM_TRIGGER_CHECK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Monitors the status of an external process by repeatedly querying a specified view or table (passed as a parameter). It polls for a successful completion status (indicated by RUN_ERR_CODE = 0) within a given timeout period (P_WAIT_MINUTES). If the success condition is not met before the timeout, an application error is raised. It uses a sleep mechanism for polling intervals.

## Data Sources (Inputs)
- ← [[P_TRIGGER_VIEW]]


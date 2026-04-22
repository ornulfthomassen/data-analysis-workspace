# V_POWERCENTER_STATUS_CHECK

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies PowerCenter workflow or task instances that have failed (indicated by RUN_ERR_CODE > 0) within the last day for specific subject areas ('Consumer_Analytics', 'Consumer_ODS') and have not been subsequently followed by a successful run (RUN_ERR_CODE = 0). Essentially, it's used to check the status of recent PowerCenter job failures that haven't been resolved or succeeded by a later successful execution.

## Data Sources (Inputs)
- ← [[PCT_REPOSITORY.REP_TASK_INST_RUN]]


# V_POWERCENTER_STATUS_CHECK

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies PowerCenter task instances that have reported an error (RUN_ERR_CODE > 0) within the last 24 hours, specifically for 'Consumer_Analytics' or 'Consumer_ODS' subject areas, and for which no subsequent successful run (RUN_ERR_CODE = 0) has been recorded, thereby highlighting unresolved or persisting task failures.

## Data Sources (Inputs)
- ← [[PCT_REPOSITORY.REP_TASK_INST_RUN]]
| Column Name |
|---|
| TASK_TYPE_NAME |
| SUBJECT_AREA |
| WORKFLOW_NAME |
| INSTANCE_NAME |
| START_TIME |
| END_TIME |
| RUN_ERR_CODE |
| RUN_ERR_MSG |
| RUN_STATUS_CODE |
| WORKFLOW_ID |
| INSTANCE_ID |


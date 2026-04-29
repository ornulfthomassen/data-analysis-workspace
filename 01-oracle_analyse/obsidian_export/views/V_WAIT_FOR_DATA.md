# V_WAIT_FOR_DATA

**Schema:** `CCM` | **Type:** `View`

## Description
Monitors the status of a specific ETL workflow instance ('COMOYO', 'wf_User_Services_SCD_Master', 'cmd_Transfer_SAS_trigger') by retrieving the `START_TIME` and `END_TIME` of its latest successful run (within the last 35 days) from the `PCT_REPOSITORY.REP_TASK_INST_RUN` table. It also includes a 'DATA_IS_FRESH' flag which is always set to 0 based on the current script logic.

## Data Sources (Inputs)
- ← [[PCT_REPOSITORY.REP_TASK_INST_RUN]]
| Column Name |
|---|
| END_TIME |
| START_TIME |
| SUBJECT_AREA |
| WORKFLOW_NAME |
| INSTANCE_NAME |
| WORKFLOW_RUN_ID |
| RUN_ERR_MSG |
| RUN_ERR_CODE |


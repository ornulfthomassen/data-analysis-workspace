# V_TRIGGER_OCS_FREE_UNITS_DAILY

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view tracks and retrieves the daily run status and details for a specific ETL task instance named 'Trigger_File_to_SAS' within the 'wf_Postswap_OCS' workflow, under the 'OCS' subject area, from the current day. It is likely used for monitoring or reporting on the execution of this particular task.

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


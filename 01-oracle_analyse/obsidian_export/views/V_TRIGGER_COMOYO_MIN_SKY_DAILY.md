# V_TRIGGER_COMOYO_MIN_SKY_DAILY

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Monitors the run status and details of a specific daily Minsky process ('wf_PROC_MINSKY_DAILY' and 's_mUpdate_ST_TRAFFIC' within the 'COMOYO' subject area) that have started within the last 12 hours, by querying repository task instance run logs.

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


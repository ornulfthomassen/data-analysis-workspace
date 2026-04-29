# V_TRIGGER_ODS_CONNECT_ID_LINK

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Retrieves the details of the most recent run (within the last 2 days) for the specific 'wf_Connect_Id_Link' ETL workflow instance ('s_m_Connect_Id_Link') within the 'ODS' subject area, providing status, timing, and error information for monitoring purposes.

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
| INSTANCE_ID |


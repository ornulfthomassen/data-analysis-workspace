# V_TRIGGER_GALAXY_ORDER_MOB

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view retrieves recent execution details (started today) for a specific ETL task instance ('s_Order_Line_Detail_MOB_Fact') within the 'wf_Order_Line_Detail_Fact' workflow and 'CCDW_ORDER' subject area from a repository table. It effectively filters for specific task run statuses and timings.

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


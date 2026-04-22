# V_WAIT_FOR_DATA

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to monitor the status of a specific data processing workflow instance. It retrieves the start and end times of the most recent successful run (indicated by NULL error message and error code 0) of the 'cmd_Transfer_SAS_trigger' instance within the 'wf_User_Services_SCD_Master' workflow for the 'COMOYO' subject area, looking back up to 35 days. The `DATA_IS_FRESH` column, as currently defined, always returns `0`, which might indicate that the data is not considered fresh or ready for consumption from this view's perspective, or serves as a placeholder for a 'wait' condition.

## Data Sources (Inputs)
- ← [[PCT_REPOSITORY.REP_TASK_INST_RUN]]


# V_TRIGGER_COMOYO_MIN_SKY_DAILY

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Retrieves recent execution details (start/end times, status, errors) for a specific workflow instance named 's_mUpdate_ST_TRAFFIC' within the 'COMOYO' subject area and 'wf_PROC_MINSKY_DAILY' workflow, specifically for runs that started within approximately the last 12-36 hours (since yesterday noon). This view likely serves for monitoring or triggering based on the status of this particular daily data processing task.

## Data Sources (Inputs)
- ← [[PCT_REPOSITORY.REP_TASK_INST_RUN]]


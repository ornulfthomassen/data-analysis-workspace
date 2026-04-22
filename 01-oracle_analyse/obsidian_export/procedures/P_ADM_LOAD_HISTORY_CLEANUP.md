# P_ADM_LOAD_HISTORY_CLEANUP

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_LOAD_HISTORY_CLEANUP`, manages records within the `CLM_ADM.ADM_LOAD_HISTORY` table. It first verifies the existence of this table. If the table exists, it retrieves the maximum `LOAD_ID` from it. Based on the `P_ACTION` parameter, it performs one of two main operations:
  - If `P_ACTION` is 'SET_OK', it updates the `JOBSTATUS` of the most recent load history entry (identified by `V_MAX_LOAD_ID`) by appending ' OK'.
  - If `P_ACTION` is 'DELETE_LAST', it deletes the most recent load history entry and then drops and re-creates the associated sequence, `CLM_ADM.ADM_LOAD_HISTORY_ID_SEQ`, resetting its `START WITH` value to the deleted `LOAD_ID`.
  For any other `P_ACTION` value or if the `CLM_ADM.ADM_LOAD_HISTORY` table does not exist, the procedure raises a division-by-zero error to halt execution.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.ADM_LOAD_HISTORY]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_LOAD_HISTORY]]


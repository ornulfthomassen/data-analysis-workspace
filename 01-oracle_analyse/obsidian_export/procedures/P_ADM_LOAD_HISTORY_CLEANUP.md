# P_ADM_LOAD_HISTORY_CLEANUP

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure manages the `ADM_LOAD_HISTORY` table within the `CLM_ADM` schema. It first checks for the existence of this table. If found, it identifies the maximum `LOAD_ID`. Depending on the `P_ACTION` parameter, it can either update the `JOBSTATUS` of the latest entry to include ' OK' (if `P_ACTION` is 'SET_OK') or delete the latest entry and recreate its associated sequence `CLM_ADM.ADM_LOAD_HISTORY_ID_SEQ`, resetting its starting value based on the previous maximum load ID (if `P_ACTION` is 'DELETE_LAST'). If the table is not found or `P_ACTION` is not recognized, it raises an error.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CLM_ADM.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |
| JOBSTATUS |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| JOBSTATUS |


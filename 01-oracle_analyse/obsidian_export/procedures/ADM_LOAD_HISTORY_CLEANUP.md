# ADM_LOAD_HISTORY_CLEANUP

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Manages and cleans up entries in the `CRM_ANALYSE.ADM_LOAD_HISTORY` table based on the specified action. It can update job statuses to 'OK', or delete the most recent load history entry and re-sequence its ID.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| LOAD_ID |
| JOBSTATUS |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| JOBSTATUS |


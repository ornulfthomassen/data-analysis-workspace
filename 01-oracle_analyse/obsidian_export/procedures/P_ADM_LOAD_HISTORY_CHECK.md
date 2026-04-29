# P_ADM_LOAD_HISTORY_CHECK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Waits for active or erroneous jobs in the `CRM_ANALYSE.ADM_LOAD_HISTORY` table to complete or resolve their status to 'OK' within a specified timeout period. It repeatedly checks the `JOBSTATUS` column. If jobs remain in a non-'OK' status after the timeout, an application error is raised.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_LOAD_HISTORY]]
| Column Name |
|---|
| JOBSTATUS |


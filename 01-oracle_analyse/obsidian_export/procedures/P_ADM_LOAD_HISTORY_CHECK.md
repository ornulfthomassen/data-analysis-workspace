# P_ADM_LOAD_HISTORY_CHECK

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_LOAD_HISTORY_CHECK`, is designed to monitor the status of data load jobs recorded in the `CRM_ANALYSE.ADM_LOAD_HISTORY` table. It repeatedly queries this table to count any jobs that are not in an 'OK' status. The procedure includes a waiting mechanism, pausing for a specified duration (`P_WAIT_MINUTES`) for these jobs to complete or transition to an 'OK' state. If, after the defined waiting period, there are still jobs with a non-'OK' status, the procedure raises an application error, indicating a potential issue with concurrent or previously run data loads.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_LOAD_HISTORY]]


# P_ADM_MIN_SKY_FIRST_USE_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes raw event data from 'COMOYO.COMOYO_SUB_GRANT_EVENTS' to identify and record the first occurrence of a specific 'RightUsed' event for each unique user and grantor. It aggregates the minimum event time, load date, and SKUs for these first events. The processed data is first stored in a temporary table 'TMP_MIN_SKY_FIRST_USE_HIST' (dropping it if it already exists). It then inserts new, previously unrecorded events from this temporary table into the main historical table 'ADM_MIN_SKY_FIRST_USE_HIST'. The procedure includes error handling, transaction management (commit/rollback), and analysis of the target table after a successful insert.

## Data Sources (Inputs)
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
- ← [[ADM_MIN_SKY_FIRST_USE_HIST]]

## Target Tables (Outputs)
- → [[TMP_MIN_SKY_FIRST_USE_HIST]]
- → [[ADM_MIN_SKY_FIRST_USE_HIST]]


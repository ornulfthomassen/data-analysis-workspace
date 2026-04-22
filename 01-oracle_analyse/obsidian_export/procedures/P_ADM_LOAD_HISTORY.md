# P_ADM_LOAD_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_LOAD_HISTORY functions as an ETL job logging and monitoring utility. It tracks the status and various statistics of data loading processes for a specified target table (referenced by the P_ETL_TABLE parameter). It records details such as job status ('RUNNING', 'ENDED OK', 'WARNING', 'ERROR'), start/end timestamps, duration, session information, and row counts (before and after the load) into the `CLM_ADM.ADM_LOAD_HISTORY` table. The procedure dynamically calculates percentage differences in row counts (current vs. prior period, current vs. historical maximum) for the `P_ETL_TABLE`. Based on these comparisons and predefined thresholds (e.g., >5% change from prior period, >3% change from max), it automatically assigns a job status of 'WARNING' or 'ERROR'; otherwise, it defaults to 'ENDED OK'. It supports two main modes: initiating a new load by inserting a 'RUNNING' entry or updating an existing load's entry with final status and metrics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_LOAD_HISTORY]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[USER_TAB_COLS]]
- ← [[P_ETL_TABLE (this refers to the table dynamically passed as a parameter, which is queried for row counts and column existence, e.g., 'YOUR_SCHEMA.YOUR_TABLE')]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_LOAD_HISTORY]]


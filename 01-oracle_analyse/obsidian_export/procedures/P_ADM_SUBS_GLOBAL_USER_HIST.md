# P_ADM_SUBS_GLOBAL_USER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_SUBS_GLOBAL_USER_HIST, is designed to process and load historical user subscription data into a specific monthly partition of the 'ADM_SUBS_GLOBAL_USER_HIST' table. It first validates the existence and integrity of source data for a given period (P_YYYYMM) from 'ADM_MONTH_DIM_V' and 'ADM_GLOBAL_USER_SUBS_HIST'. If validation passes, it performs cleanup by dropping any pre-existing temporary table ('TMP_SUBS_GLOBAL_USER_HIST'). It then creates a new temporary table ('TMP_SUBS_GLOBAL_USER_HIST') by aggregating and joining data from 'ADM_GLOBAL_USER_SUBS_HIST' and 'ADM_CONNECT_ID_HIST' for the specified month. Finally, it uses an 'ALTER TABLE EXCHANGE PARTITION' command to swap this temporary table with a partition (which is either added if not present or prepared for overwrite) in the main 'ADM_SUBS_GLOBAL_USER_HIST' table, effectively loading the processed data. Statistics are then computed for the newly loaded partition.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_GLOBAL_USER_SUBS_HIST]]
- ← [[CLM_ADM.ADM_CONNECT_ID_HIST]]
- ← [[ADM_SUBS_GLOBAL_USER_HIST]]

## Target Tables (Outputs)
- → [[ADM_SUBS_GLOBAL_USER_HIST]]
- → [[TMP_SUBS_GLOBAL_USER_HIST]]


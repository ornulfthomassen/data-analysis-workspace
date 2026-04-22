# P_ADM_CUSTOMER_CORE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure (`P_ADM_CUSTOMER_CORE`) is designed to create or refresh a specific monthly partition within a master customer core table (`ADM_CUSTOMER_CORE`). It first checks for the existence of the target table and its partition. If the partition already exists, it can either error out (if it contains data and overwrite is not allowed) or proceed. It then builds a temporary staging table (`TMP_CUSTOMER_CORE`) by selecting and transforming data from various CRM/CLM analytic dimensions and history tables for the specified month. Finally, it uses a partition exchange operation to efficiently replace or load the data from the temporary table into the corresponding monthly partition of the permanent `ADM_CUSTOMER_CORE` table, and then gathers statistics on the newly loaded partition.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_CORE]]
- → [[TMP_CUSTOMER_CORE]]


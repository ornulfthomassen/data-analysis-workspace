# HH_TAB_CRM_ANALYSE_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `HH_TAB_CRM_ANALYSE_2_CLM_ADM` performs a data migration and transformation process. For a given range of month keys, it reads data from a source table (specified by `P_TABLE_OLD` and `P_FRA_SCHEMA`), joins it with household mapping data from `CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST`, and transforms it. The transformed data is then loaded into a target partitioned table (specified by `P_TABLE_NEW` and `P_TIL_SCHEMA`). It handles the dynamic creation of the target table and its partitions, uses a temporary table (`P_TMP_TABLE`) for intermediate storage before performing an exchange partition operation, and logs the entire migration process in `ADM_MIGRATE_LOG`.

## Data Sources (Inputs)
- ← [[ALL_TAB_COLS]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[P_TABLE_OLD]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
- ← [[ADM_MIGRATE_LOG]]

## Target Tables (Outputs)
- → [[P_TABLE_NEW]]
- → [[P_TMP_TABLE]]
- → [[ADM_MIGRATE_LOG]]


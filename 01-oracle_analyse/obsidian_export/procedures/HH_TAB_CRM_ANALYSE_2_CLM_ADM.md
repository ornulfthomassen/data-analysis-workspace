# HH_TAB_CRM_ANALYSE_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Migrates data from a partitioned source table (CRM_ANALYSE.P_TABLE_OLD) to a new, similarly partitioned target table (CLM_ADM.P_TABLE_NEW). It performs data enrichment by joining with household mapping historical data (CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST) to derive household address and unit surrogate keys. The procedure processes data month by month, creating the target table if it doesn't exist, managing partitions by exchanging data through a temporary table, and logging migration status and statistics in ADM_MIGRATE_LOG.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[ALL_TAB_COLS]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| COLUMN_ID |
| COLUMN_NAME |
| DATA_TYPE |
| DATA_LENGTH |
| NULLABLE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| <P_HH_ID_COLUMN1> |
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| HOUSEHOLD_ID |
- ← [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
- ← [[<P_TMP_TABLE>]]

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| <P_HH_ADDR_SK_COLUMN1> |
| <P_HH_UNIT_SK_COLUMN1> |
- → [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
| MIGRATE_DTTM_START |
| FROM_TABLE |
| TO_TABLE |
| FROM_NUM_COLUMNS |
| TO_NUM_COLUMNS |
| PERIOD_MONTH_KEY |
| FROM_NUM_ROWS |
| STATUS |
| MIGRATE_DTTM_END |
| TO_NUM_ROWS |
- → [[<P_TMP_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| <P_HH_ADDR_SK_COLUMN1> |
| <P_HH_UNIT_SK_COLUMN1> |


# SUBS_TAB_CLM_ADM_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure facilitates the migration of historical data for a specified range of months (YYYYMM_FRA to YYYYMM_TIL) from a source table (P_TABLE_OLD) to a target partitioned table (P_TABLE_NEW), both residing in the CLM_ADM schema. It dynamically constructs the target table schema based on the source table, explicitly handling 'PERIOD_MONTH_KEY' and 'SUBSCRIPTION_ID' columns, while excluding certain others (e.g., those containing 'KURT_ID', 'KURT_SK', 'MAIN_NUMBER'). If the target table does not exist, it creates it as a list-partitioned table. For each month, it creates a temporary table populated with data from the source table's corresponding partition, and then performs a partition exchange to load the data into the target table. The process includes logging of migration steps and statistics in the ADM_MIGRATE_LOG table, and collecting statistics on the new partitions.

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
| COLUMN_ID |
| COLUMN_NAME |
| DATA_TYPE |
| DATA_LENGTH |
| NULLABLE |
| OWNER |
| TABLE_NAME |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
- ← [[P_TABLE_OLD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |

## Target Tables (Outputs)
- → [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
| MIGRATE_DTTM_START |
| MIGRATE_DTTM_END |
| FROM_TABLE |
| TO_TABLE |
| FROM_NUM_COLUMNS |
| TO_NUM_COLUMNS |
| PERIOD_MONTH_KEY |
| FROM_NUM_ROWS |
| TO_NUM_ROWS |
| STATUS |
| ERROR_MESSAGE |
- → [[P_TABLE_NEW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
- → [[P_TMP_TABLE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |


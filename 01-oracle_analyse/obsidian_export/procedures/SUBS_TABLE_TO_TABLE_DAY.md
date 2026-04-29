# SUBS_TABLE_TO_TABLE_DAY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure migrates or copies data on a partition-by-partition basis from a source table (P_TABLE_OLD) to a new target table (P_TABLE_NEW) for a specified date range (P_YYYYMM_FRA to P_YYYYMM_TIL). It dynamically creates the target table and its partitions if they don't exist, extracts columns from the source (excluding specific ones), adds PERIOD_DATE_KEY and SUBSCRIPTION_ID, and loads them into a temporary table. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently move the data from the temporary table into the corresponding partition of the target table.

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
| COLUMN_NAME |
| DATA_TYPE |
| DATA_LENGTH |
| NULLABLE |
| COLUMN_ID |
| OWNER |
| TABLE_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
- ← [[P_TABLE_OLD]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| *(all other columns except DATE_KEY, KURT_ID, MAIN_NUMBER)* |

## Target Tables (Outputs)
- → [[P_TABLE_NEW]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
| SUBSCRIPTION_ID |
| *(all other columns from P_TABLE_OLD except DATE_KEY, KURT_ID, MAIN_NUMBER)* |
- → [[P_TMP_TABLE]]
| Column Name |
|---|
| PERIOD_DATE_KEY |
| SUBSCRIPTION_ID |
| *(all other columns from P_TABLE_OLD except DATE_KEY, KURT_ID, MAIN_NUMBER)* |


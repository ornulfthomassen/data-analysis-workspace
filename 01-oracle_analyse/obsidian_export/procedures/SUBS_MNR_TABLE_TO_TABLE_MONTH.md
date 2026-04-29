# SUBS_MNR_TABLE_TO_TABLE_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure dynamically migrates and transforms monthly partitioned data. For a specified range of months, it extracts data from a source table (P_TABLE_OLD), joining it with CLM_ADM.ADM_MONTH_DIM_V and CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE. It creates a temporary table (P_TMP_TABLE) with columns derived from the source table (excluding certain filtered columns) and new PERIOD_MONTH_KEY and SUBSCRIPTION_ID columns. This temporary data is then moved into a corresponding partition of the target table (P_TABLE_NEW) using a partition exchange. The target table and its partitions are created dynamically if they do not exist.

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
| DATA_PRECISION |
| DATA_SCALE |
| NULLABLE |
| COLUMN_ID |
| OWNER |
| TABLE_NAME |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FIRST_DATE |
| LAST_DATE |
- ← [[P_TABLE_OLD]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| END_DATE |
| ORIGINAL_START_DATE |

## Target Tables (Outputs)
- → [[P_TABLE_NEW]]
- → [[P_TMP_TABLE]]


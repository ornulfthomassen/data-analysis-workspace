# CUST_TAB_CLM_ADM_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Migrates and transforms customer-related data from a source table (`P_TABLE_OLD`) to a new, partitioned target table (`P_TABLE_NEW`). It creates the target table based on the source's structure, maps customer identifiers using an `ADM_CUSTOMER_MAPPING` table for each monthly partition, and stages the transformed data in a temporary table before exchanging it into the target partition. The process is logged in `ADM_MIGRATE_LOG`.

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
| DATA_PRECISION |
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
| P_KURT_COLUMN1 |
| P_KURT_COLUMN2 |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_[PERIOD_MONTH_KEY]]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

## Target Tables (Outputs)
- → [[P_TABLE_NEW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| P_CUST_COLUMN1 |
| P_CUST_COLUMN2 |
- → [[P_TMP_TABLE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| P_CUST_COLUMN1 |
| P_CUST_COLUMN2 |
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


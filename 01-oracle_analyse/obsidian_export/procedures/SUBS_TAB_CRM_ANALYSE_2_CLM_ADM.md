# SUBS_TAB_CRM_ANALYSE_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure migrates and transforms monthly data for a specified period (P_YYYYMM_FRA to P_YYYYMM_TIL) from a source table (`CRM_ANALYSE.P_TABLE_OLD`) into a partitioned target table (`CLM_ADM.P_TABLE_NEW`). It enriches subscription and customer information by joining with master and mapping tables, dynamically creating the target table and its partitions if they don't exist, using a temporary table for intermediate data processing, and logging the migration activities.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[SYS.ALL_TAB_COLS]]
| Column Name |
|---|
| COLUMN_ID |
| OWNER |
| TABLE_NAME |
| COLUMN_NAME |
| DATA_TYPE |
| DATA_LENGTH |
| NULLABLE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[ADM_MIGRATE_LOG]]
| Column Name |
|---|
| AML_ID |
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| <P_KURT_COLUMN1> |
| <P_KURT_COLUMN2> |
| All other columns from the source table (CRM_ANALYSE.<P_TABLE_OLD>) whose names do not exactly match 'MAIN_NUMBER' and do not contain 'KURT_ID', 'KURT_SK', 'MAIN_NUMBER', 'SMALLSCR', or 'SMALL_SCR' as substrings. |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_<YYYYMM>]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| <P_CUST_COLUMN1> |
| <P_CUST_COLUMN2> |
| All other columns from the source table (CRM_ANALYSE.<P_TABLE_OLD>) whose names do not exactly match 'MAIN_NUMBER' and do not contain 'KURT_ID', 'KURT_SK', 'MAIN_NUMBER', 'SMALLSCR', or 'SMALL_SCR' as substrings. |
- → [[<P_TMP_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| <P_CUST_COLUMN1> |
| <P_CUST_COLUMN2> |
| All other columns from the source table (CRM_ANALYSE.<P_TABLE_OLD>) whose names do not exactly match 'MAIN_NUMBER' and do not contain 'KURT_ID', 'KURT_SK', 'MAIN_NUMBER', 'SMALLSCR', or 'SMALL_SCR' as substrings. |
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


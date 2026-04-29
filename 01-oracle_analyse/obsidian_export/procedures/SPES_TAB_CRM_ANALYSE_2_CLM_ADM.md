# SPES_TAB_CRM_ANALYSE_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure migrates partitioned data from a source table in the CRM_ANALYSE schema to a target partitioned table in the CLM_ADM schema. For each specified month, it creates a temporary table, populates it by joining the source data with customer mapping and subscription master history tables, transforms specific customer ID columns using mapping, and then exchanges this temporary table with a corresponding partition in the target table. It also handles target table/partition creation and logs the migration process.

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
| DATA_PRECISION |
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
- ← [[V_FRA_SCHEMA.V_TABLE_OLD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| P_KURT_COLUMN1 |
| P_KURT_COLUMN2 |
| P_KURT_COLUMN3 |
| P_KURT_COLUMN4 |
| P_KURT_COLUMN5 |
| P_KURT_COLUMN6 |
| P_KURT_COLUMN7 |
| P_KURT_COLUMN8 |
| P_KURT_COLUMN9 |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_{ITEM.PERIOD_MONTH_KEY}]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

## Target Tables (Outputs)
- → [[V_TIL_SCHEMA.V_TABLE_NEW]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| P_CUST_COLUMN1 |
| P_CUST_COLUMN2 |
| P_CUST_COLUMN3 |
| P_CUST_COLUMN4 |
| P_CUST_COLUMN5 |
| P_CUST_COLUMN6 |
| P_CUST_COLUMN7 |
| P_CUST_COLUMN8 |
| P_CUST_COLUMN9 |
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
- → [[V_TMP_TABLE]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| P_CUST_COLUMN1 |
| P_CUST_COLUMN2 |
| P_CUST_COLUMN3 |
| P_CUST_COLUMN4 |
| P_CUST_COLUMN5 |
| P_CUST_COLUMN6 |
| P_CUST_COLUMN7 |
| P_CUST_COLUMN8 |
| P_CUST_COLUMN9 |


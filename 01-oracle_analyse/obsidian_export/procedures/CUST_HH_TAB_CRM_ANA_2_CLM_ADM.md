# CUST_HH_TAB_CRM_ANA_2_CLM_ADM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure migrates and transforms data from a source table specified by the `P_TABLE_OLD` parameter (expected in `CRM_ANALYSE` schema) into a new partitioned target table specified by the `P_TABLE_NEW` parameter (expected in `CLM_ADM` schema). It processes data for a given range of months (from `P_YYYYMM_FRA` to `P_YYYYMM_TIL`), iterating month by month. For each month, it joins the source data with customer and household mapping/dimension tables (`CLM_ADM.ADM_CUSTOMER_MAPPING_<YYYYMM>`, `CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST`, `CRM_ANALYSE.RM_HOUSEHOLD_INFO_HIST`). It performs data transformations such as mapping `KURT_ID` to `CUSTOMER_SK`, `HOUSEHOLD_ID` to `HOUSEHOLD_ADDR_SK` and `HOUSEHOLD_UNIT_SK`, and derives a flag `CU_HH_SAME_ADDR_FLG` based on postcode. The procedure dynamically identifies and copies most other columns from the source table to the target, excluding certain common identifier and system columns. The processed data is first loaded into a temporary table (`P_TMP_TABLE`), which then replaces a specific partition in the permanent target table using an `EXCHANGE PARTITION` operation. The procedure also handles the creation of the target table and its partitions if they do not exist, grants SELECT privileges, analyzes statistics, and logs the migration process status and row counts into `ADM_MIGRATE_LOG`.

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
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| <P_KURT_COLUMN1> |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_<YYYYMM>]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CLM_ADM.ADM_HOUSEHOLD_MAPPING_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
- ← [[CRM_ANALYSE.RM_HOUSEHOLD_INFO_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| POSTNR |

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| <P_CUST_COLUMN1> |
| <P_HH_ADDR_SK_COLUMN> |
| <P_HH_UNIT_SK_COLUMN> |
| CU_HH_SAME_ADDR_FLG |
| POSTNR |
| All other columns from CRM_ANALYSE.<P_TABLE_OLD> except 'MAIN_NUMBER', 'SUBSCRIPTION_ID', and those containing 'HOUSEHOLD_ID', 'KURT_ID', 'KURT_SK', 'X_KRID', 'MAIN_NUMBER', 'SMALLSCR', 'SMALL_SCR', 'SYS_NC0005' in their name. |
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
- → [[<P_TMP_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| <P_CUST_COLUMN1> |
| <P_HH_ADDR_SK_COLUMN> |
| <P_HH_UNIT_SK_COLUMN> |
| CU_HH_SAME_ADDR_FLG |
| POSTNR |
| All other columns from CRM_ANALYSE.<P_TABLE_OLD> except 'PERIOD_MONTH_KEY', 'MAIN_NUMBER', 'SUBSCRIPTION_ID', and those containing 'HOUSEHOLD_ID', 'KURT_ID', 'KURT_SK', 'X_KRID', 'MAIN_NUMBER', 'SMALLSCR', 'SMALL_SCR', 'SYS_NC0005' in their name. |


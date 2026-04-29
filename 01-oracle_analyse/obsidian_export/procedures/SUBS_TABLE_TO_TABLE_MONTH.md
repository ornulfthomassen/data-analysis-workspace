# SUBS_TABLE_TO_TABLE_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure efficiently copies data from a specified source partitioned table (P_TABLE_OLD) to a target partitioned table (P_TABLE_NEW) on a monthly basis. It dynamically discovers the source table's column structure, creates the target table and its partitions if they don't exist, filters out specific columns during the transfer, uses a temporary table for data staging, and performs partition exchange to load data into the target for a given month range. It also manages table parallelism and grants SELECT privileges on the target table.

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
- ← [[CRM_ANALYSE.<P_TABLE_OLD>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| ALL OTHER COLUMNS EXCEPT: 'MAIN_NUMBER' (exact match), or columns containing 'KURT_ID' or 'MAIN_NUMBER' as substrings. |

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| ALL OTHER COLUMNS EXCEPT: 'MAIN_NUMBER' (exact match), or columns containing 'KURT_ID' or 'MAIN_NUMBER' as substrings. |
- → [[CLM_ADM.<P_TMP_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| ALL OTHER COLUMNS EXCEPT: 'MAIN_NUMBER' (exact match), or columns containing 'KURT_ID' or 'MAIN_NUMBER' as substrings. |


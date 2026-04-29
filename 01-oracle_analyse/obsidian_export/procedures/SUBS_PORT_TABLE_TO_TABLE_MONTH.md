# SUBS_PORT_TABLE_TO_TABLE_MONTH

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure ports monthly partitioned data from a source table (`P_TABLE_OLD` in schema `CRM_ANALYSE`) to a target table (`P_TABLE_NEW` in schema `CLM_ADM`). It enriches the source data by joining with subscription history tables (`ADM_SUBSCRIPTION_HISTORY`, `ADM_SUBSCRIPTION_HISTORY_I`). The process dynamically creates the target table if it doesn't exist, adds partitions for each month within a specified range (`P_YYYYMM_FRA` to `P_YYYYMM_TIL`), and populates these partitions efficiently using a temporary table (`P_TMP_TABLE`) and an `ALTER TABLE ... EXCHANGE PARTITION` operation. It excludes specific columns ('PERIOD_MONTH_KEY', 'MAIN_NUMBER', 'SUBSCRIPTION_ID', and those containing 'KURT_ID') from the direct copy, while explicitly adding `PERIOD_MONTH_KEY` and `SUBSCRIPTION_ID` to the target.

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
| MAIN_NUMBER |
| (all other columns from P_TABLE_OLD except 'PERIOD_MONTH_KEY', 'MAIN_NUMBER', 'SUBSCRIPTION_ID', and columns containing 'KURT_ID') |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PERIOD_MONTH_KEY |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_I]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| PERIOD_MONTH_KEY |

## Target Tables (Outputs)
- → [[CLM_ADM.<P_TABLE_NEW>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| (all columns from P_TABLE_OLD except 'PERIOD_MONTH_KEY', 'MAIN_NUMBER', 'SUBSCRIPTION_ID', and columns containing 'KURT_ID') |
- → [[CLM_ADM.<P_TMP_TABLE>]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| (all columns from P_TABLE_OLD except 'PERIOD_MONTH_KEY', 'MAIN_NUMBER', 'SUBSCRIPTION_ID', and columns containing 'KURT_ID') |


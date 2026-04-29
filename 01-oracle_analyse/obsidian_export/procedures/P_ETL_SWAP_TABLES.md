# P_ETL_SWAP_TABLES

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Performs a "zero-downtime" table swap by renaming a newly prepared staging table (suffixed with '_N') to become the live target table, and renaming the current live table to a backup (suffixed with '_O'). The procedure includes row count validation based on a threshold, creation and renaming of indexes, granting of privileges, and gathering of table statistics, with comprehensive logging in case of errors or warnings.

## Data Sources (Inputs)
- ← [[P_SCHEMA.P_TABLE_T]]
- ← [[P_SCHEMA.V_TABLE_N]]
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |

## Target Tables (Outputs)
- → [[P_SCHEMA.V_TABLE_N]]
- → [[P_SCHEMA.V_TABLE_O]]
- → [[P_SCHEMA.P_TABLE_T]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| STATUS |
| MESSAGE |
| WORKFLOW_NAME |
| SESSION_NAME |


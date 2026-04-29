# ADM_MAKE_BACKUP_TABLE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Renames an existing Oracle table and its associated indexes to a new specified name, effectively creating a backup or historical version of the table. It performs comprehensive validation on the provided table names and checks for potential naming conflicts with existing database objects before executing the DDL operations. It returns status codes and error messages based on the outcome.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
- ← [[DBA_IND_COLUMNS]]
| Column Name |
|---|
| TABLE_NAME |
| TABLE_OWNER |
| INDEX_NAME |

## Target Tables (Outputs)
- → [[P_TABLENAME_O]]


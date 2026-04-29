# DROP_TMP_TABLE_IF_EXIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Checks for the existence of a table (prefixed with 'TMP_') in the current schema based on an input parameter, and if found, dynamically drops that table.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |


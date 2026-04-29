# F_DELETE_IF_EXIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Checks for the existence of a specified table or view within the 'CLM_ADM' schema and drops it if found. This function performs DDL (Data Definition Language) operations (DROP TABLE, DROP VIEW) based on the input parameter.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |


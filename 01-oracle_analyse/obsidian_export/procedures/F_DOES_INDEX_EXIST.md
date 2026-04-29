# F_DOES_INDEX_EXIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Checks for the existence of an index by a given name within the current database schema. It returns 1 if an index with that name exists, and 0 otherwise.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |


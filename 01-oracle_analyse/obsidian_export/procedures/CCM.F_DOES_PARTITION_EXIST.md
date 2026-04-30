# F_DOES_PARTITION_EXIST

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Checks if a specified table partition exists within the current database schema. It returns 1 if the partition exists for the given table, and 0 otherwise.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| SUBOBJECT_NAME |
| OWNER |



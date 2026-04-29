# F_DOES_PARTITION_EXIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Checks for the existence of a specified table partition within the current schema. It returns 1 if the partition exists, and 0 otherwise.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| SUBOBJECT_NAME |
| OWNER |


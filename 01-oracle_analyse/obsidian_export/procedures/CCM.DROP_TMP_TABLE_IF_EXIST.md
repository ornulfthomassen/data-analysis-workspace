# DROP_TMP_TABLE_IF_EXIST

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure checks for the existence of a table, identified by the input parameter `P_TABLE`, within the current user's schema. If the table is found, it is subsequently dropped using dynamic SQL.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |



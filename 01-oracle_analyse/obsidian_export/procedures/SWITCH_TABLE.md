# SWITCH_TABLE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Renames a specified table (P_OLD_TABLE_NAME) to a new name (P_NEW_TABLE_NAME) within the given schema (P_TABLE_OWNER). The procedure verifies that the old table exists and that the new table name does not already exist in the specified schema. If the new table name is already in use, the procedure terminates with an error, preventing an overwrite. The P_FORCE_SWITCH parameter, despite its name, does not enable forceful renaming over an existing table with the current logic.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OWNER |
| OBJECT_NAME |
| OBJECT_TYPE |

## Target Tables (Outputs)
- → [[<P_OLD_TABLE_NAME (dynamically determined from parameter)>]]


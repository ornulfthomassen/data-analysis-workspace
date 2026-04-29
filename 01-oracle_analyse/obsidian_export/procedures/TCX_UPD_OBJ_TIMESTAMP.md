# TCX_UPD_OBJ_TIMESTAMP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Updates the 'OBJECT_TIMESTAMP' column in the 'CCM.TCX_CONFIG' table to the current system date. This update is triggered automatically after any INSERT, DELETE, or UPDATE operation on a row in the 'CCM.TCX_OBJECTS' table, affecting the corresponding configuration record identified by the 'CONFIG_ID' from the affected 'CCM.TCX_OBJECTS' row.

## Data Sources (Inputs)
- ← [[CCM.TCX_OBJECTS]]
| Column Name |
|---|
| CONFIG_ID |

## Target Tables (Outputs)
- → [[CCM.TCX_CONFIG]]
| Column Name |
|---|
| OBJECT_TIMESTAMP |


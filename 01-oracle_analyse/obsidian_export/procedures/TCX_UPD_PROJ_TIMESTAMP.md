# TCX_UPD_PROJ_TIMESTAMP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This trigger updates the 'OBJECT_TIMESTAMP' column in the 'CCM.TCX_CONFIG' table to the current system date and time. This update occurs whenever an INSERT, UPDATE, or DELETE operation is performed on the 'CCM.TCX_TEAM_PROJECTS' table. The specific row updated in 'CCM.TCX_CONFIG' is determined by matching its 'CONFIG_ID' with the 'CONFIG_ID' from the row being modified in 'CCM.TCX_TEAM_PROJECTS'.

## Data Sources (Inputs)
- ← [[CCM.TCX_TEAM_PROJECTS]]
| Column Name |
|---|
| CONFIG_ID |

## Target Tables (Outputs)
- → [[CCM.TCX_CONFIG]]
| Column Name |
|---|
| OBJECT_TIMESTAMP |


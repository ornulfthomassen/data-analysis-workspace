# KIM_SUBS_TRAFFIC_GROUP

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a categorized lookup or dimension table for subscriber traffic groups. It retrieves base traffic group definitions (ID, Name, Description, Value_from, Value_to) from the ANALYTICAL_GROUP_DIM table, specifically for `type_ID = 10`. It then enriches these groups by deriving human-readable descriptions (GROUP_DESC: e.g., LOW, MED, HIGH) and explicit traffic volume ranges (GROUP_RANGES: e.g., ' 05 - 49,99 MB') based on the group's name. Additionally, it includes two placeholder rows with negative keys (-1, -2) and 'missing' values, likely to handle cases of unknown or unassigned traffic groups in reporting or analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ANALYTICAL_GROUP_DIM]]


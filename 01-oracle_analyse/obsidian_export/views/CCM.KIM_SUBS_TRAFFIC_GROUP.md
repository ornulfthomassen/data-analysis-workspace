# KIM_SUBS_TRAFFIC_GROUP

**Schema:** `CCM` | **Type:** `View`

## Description
This view defines and categorizes 'traffic groups' based on an analytical dimension. It combines specific entries from 'ANALYTICAL_GROUP_DIM' (where type_ID is 10) with two additional hardcoded 'missing' entries, providing descriptive labels (GROUP_DESC) and traffic ranges (GROUP_RANGES) derived from the 'Name' column.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ANALYTICAL_GROUP_DIM]]
| Column Name |
|---|
| ID |
| Name |
| Description |
| Value_from |
| value_to |
| type_ID |

- ← [[CCM.DUAL]]


# KIM_ORDER_STATUS_RANK_V

**Schema:** `CCM` | **Type:** `View`

## Description
Categorizes order statuses into a numerical rank based on their type code. Assigns rank 1 to 'FERDIG' and 'ARKIVERT' statuses, rank 2 to several in-progress or pending statuses, and rank 3 to all other statuses.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| ORDER_STATUS_KEY |
| ORDER_STATUS_TYPE_CODE |


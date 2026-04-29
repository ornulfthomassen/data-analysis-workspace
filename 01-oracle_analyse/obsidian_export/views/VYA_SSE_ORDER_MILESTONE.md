# VYA_SSE_ORDER_MILESTONE

**Schema:** `CCM` | **Type:** `View`

## Description
This view transforms order-related milestone data from the `KAPAKS.SSE_MILESTONE` table. It pivots rows corresponding to specific milestone IDs (14, 102, 290) into columns, creating a wide format where each milestone's name, actual, baseline, planned, state, and comments are presented as distinct columns.

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_MILESTONE]]
| Column Name |
|---|
| OBJECTID |
| MID |
| MILESTONE |
| STATE |
| BASELINE |
| PLANNED |
| ACTUAL |
| COMMENTS |
| OBJECTTYPE |


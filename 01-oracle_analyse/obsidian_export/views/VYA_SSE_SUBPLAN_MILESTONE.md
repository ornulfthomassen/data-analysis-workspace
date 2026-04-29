# VYA_SSE_SUBPLAN_MILESTONE

**Schema:** `CCM` | **Type:** `View`

## Description
This view pivots specific milestone data for 'SubPlan' objects from the KAPAKS.SSE_MILESTONE table. It transforms rows corresponding to predefined milestone IDs (243, 244, 245, 254, 315, 332) into a wider format, creating distinct columns for milestone name, actual, baseline, planned, state, and comments for each of these milestone IDs, grouped by object ID (SPID).

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


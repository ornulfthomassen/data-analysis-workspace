# VYA_SSE_SUBPLAN_ROLE

**Schema:** `CCM` | **Type:** `View`

## Description
Pivots user IDs and display names from the `KAPAKS.SSE_OBJECTROLE` table, specifically for roles associated with 'SubPlan' objects, transforming multiple role entries into distinct columns for each role (e.g., 'CON-PL', 'CON-KAM', 'NP-FIBER', 'NR-SM'). This provides a consolidated, wide view of subplan roles.

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_OBJECTROLE]]
| Column Name |
|---|
| OBJECTID |
| ROLENAME |
| USERID |
| DISPLAYNAME |
| OBJECTTYPE |


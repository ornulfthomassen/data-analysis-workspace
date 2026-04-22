# VYA_SSE_SUBPLAN_ROLE

**Schema:** `CCM` | **Type:** `View`

## Description
This view denormalizes role-based user assignments for 'SubPlan' objects. It pivots rows containing user IDs and display names for specific roles ('CON-PL', 'CON-KAM', 'NP-FIBER', 'NR-SM') associated with a 'SubPlan' into distinct columns, providing a wide format where each SubPlan's roles and their corresponding user/display names are presented on a single row.

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_OBJECTROLE]]


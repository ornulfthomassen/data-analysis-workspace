# VYA_SSE_SUBPLAN_MILESTONE

**Schema:** `CCM` | **Type:** `View`

## Description
This view transforms detailed milestone data for specific 'SubPlan' objects from a row-based format into a column-based (pivoted) format. It extracts milestone name, actual, baseline, planned dates/values, state, and comments for a predefined set of milestone IDs (243, 244, 245, 254, 315, 332), presenting each milestone's attributes as separate columns for every unique SubPlan ID (SPID). This provides a wide, consolidated view of key milestone details for each SubPlan.

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_MILESTONE]]


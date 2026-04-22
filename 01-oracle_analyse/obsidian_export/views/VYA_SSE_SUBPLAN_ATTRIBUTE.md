# VYA_SSE_SUBPLAN_ATTRIBUTE

**Schema:** `CCM` | **Type:** `View`

## Description
Flattens and pivots attribute data for 'SubPlan' objects. It transforms rows from the source table, where each row represents a specific attribute (identified by AID), into distinct columns. This provides a wide format view of 'SubPlan' attributes, including their name, group name, value, and update details, for a predefined set of attribute IDs.

## Data Sources (Inputs)
- ← [[KAPAKS.TMP_SSE_ATTRIBUTE]]


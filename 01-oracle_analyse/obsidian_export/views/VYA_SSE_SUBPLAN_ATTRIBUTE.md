# VYA_SSE_SUBPLAN_ATTRIBUTE

**Schema:** `CCM` | **Type:** `View`

## Description
Pivots subplan-related attribute data from a source attribute table (TMP_SSE_ATTRIBUTE) into a wide, denormalized format. It transforms rows containing specific attribute IDs (AID) and their associated metadata (name, group, value, update details) into distinct columns for easier consumption, effectively creating a row for each subplan with all its relevant pivoted attributes.

## Data Sources (Inputs)
- ← [[KAPAKS.TMP_SSE_ATTRIBUTE]]
| Column Name |
|---|
| OBJECTID |
| AID |
| ATTRIBUTENAME |
| GROUPNAME |
| ATTRVALUE |
| UPDATEDBY |
| UPDATED_DATE |
| OBJECTTYPE |


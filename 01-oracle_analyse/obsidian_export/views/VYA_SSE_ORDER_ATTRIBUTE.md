# VYA_SSE_ORDER_ATTRIBUTE

**Schema:** `CCM` | **Type:** `View`

## Description
Transforms specific order attributes (identified by AID) from the `KAPAKS.TMP_SSE_ATTRIBUTE` table from a row-based format into a column-based (pivoted) format, providing a flattened view of order attributes associated with 'Orders' objects.

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


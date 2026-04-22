# VYA_SSE_ORDER_ATTRIBUTE

**Schema:** `CCM` | **Type:** `View`

## Description
Transforms and pivots specific order attributes from a generic attribute table into a wide format. It extracts attributes (Name, Group Name, Value, Last Updated, Updated By) for a predefined set of Attribute IDs (AIDs 912, 914, 1814, 1815, 1828, 1832, 1834, 1949) related to 'Orders' and presents each attribute's details as separate columns, identified by the AID.

## Data Sources (Inputs)
- ← [[KAPAKS.TMP_SSE_ATTRIBUTE]]


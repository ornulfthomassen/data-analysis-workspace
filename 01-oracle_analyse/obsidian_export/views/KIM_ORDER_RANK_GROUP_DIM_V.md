# KIM_ORDER_RANK_GROUP_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view for order rank groups, standardizing 'ORDER_RANK_GROUP' and 'ORDER_RANK_GROUP_DESC' columns by replacing NULLs with '-1' and ensuring specific VARCHAR2 data types for these descriptive attributes. It provides a consistent interface to the underlying order rank group dimension table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_ORDER_RANK_GROUP_DIM]]


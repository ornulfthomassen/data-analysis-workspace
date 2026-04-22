# KIM_AGE_GROUP_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view defines and extracts a dimension table for age groups. It selects various attributes such as ID, name, description, value ranges (from, to), hierarchical level, parent, sorting order, and type ID. The view specifically filters records from the `ANALYTICAL_GROUP_DIM` table that are related to 'AGE' by joining the table to itself to identify parent entries with the name 'AGE'.

## Data Sources (Inputs)
- ← [[ANALYTICAL_GROUP_DIM]]


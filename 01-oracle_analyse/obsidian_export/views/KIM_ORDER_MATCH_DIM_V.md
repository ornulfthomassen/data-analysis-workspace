# KIM_ORDER_MATCH_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a standardized view of the 'KIM_ORDER_MATCH_DIM' dimension, replacing NULL values in specific string columns with '-1' (casted to VARCHAR2) and ensuring consistent data types and lengths for these attributes. This is typical for preparing dimension data for reporting or analytical purposes, ensuring no NULLs for specific attributes and consistent string formatting.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_ORDER_MATCH_DIM]]


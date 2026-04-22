# KIM_TREATMENT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed information about 'treatments' and their associated 'treatment groups' into a single dimension view. It combines attributes from two source tables, standardizing null values for many string columns by replacing them with the string '-1'. This unified view is likely intended for analytical reporting or data warehousing purposes, providing a comprehensive set of treatment-related attributes.

## Data Sources (Inputs)
- ← [[KIM_TREATMENT_DIM]]
- ← [[KIM_TREATMENT_GROUP_DIM]]


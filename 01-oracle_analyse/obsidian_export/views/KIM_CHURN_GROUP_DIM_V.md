# KIM_CHURN_GROUP_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts specific churn group dimension attributes (key, name, description) by selecting and renaming columns from the 'ANALYTICAL_GROUP_DIM' table and filtering records where the 'TYPE_ID' is 42. It also performs data type casting for the name and description fields.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ANALYTICAL_GROUP_DIM]]


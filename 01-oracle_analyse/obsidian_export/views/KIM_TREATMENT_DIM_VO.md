# KIM_TREATMENT_DIM_VO

**Schema:** `CCM` | **Type:** `View`

## Description
This view transforms and enriches customer treatment (campaign) data. Its primary purpose is to categorize various 'treatment' types, particularly those related to retention pilot programs, into hierarchical groups (`TREATMENT_SUB_GROUP`, `TREATMENT_GROUP`, `TREATMENT_GROUP_SH`) based on the `ACTION_CATEGORY` and `TREATMENT_CD`. It also standardizes data types and handles null values for several descriptive attributes by replacing them with a default indicator ('-1'). This provides a more user-friendly and categorized dimension for analytical reporting on customer treatments.

## Data Sources (Inputs)
- ← [[KIM_TREATMENT_DIM]]


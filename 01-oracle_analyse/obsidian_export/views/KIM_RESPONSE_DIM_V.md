# KIM_RESPONSE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, KIM_RESPONSE_DIM_V, serves as a dimension view providing response-related attributes. Its primary purpose is to expose data from the KIM_RESPONSE_DIM table while applying data standardization. Specifically, it handles null values for 'RESPONSE_CD', 'RESPONSE_GROUP', 'RESPONSE_NM', and 'CURRENT_STATUS' by replacing them with '-1' and explicitly casts these and other relevant columns to VARCHAR2 data types, ensuring data consistency for reporting or analytical purposes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]


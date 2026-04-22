# KIM_MEASURE_TYPE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a dimension for measure types, standardizing NULL values in the 'MEASURE_TYPE_NAME' and 'MEASURE_TYPE_DESC' columns by replacing them with a placeholder ('-1') and ensuring consistent data types (VARCHAR2) and lengths for these columns. It serves to clean and prepare measure type data for reporting or analytical purposes by handling potential missing values and enforcing data consistency.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_MEASURE_TYPE_DIM]]


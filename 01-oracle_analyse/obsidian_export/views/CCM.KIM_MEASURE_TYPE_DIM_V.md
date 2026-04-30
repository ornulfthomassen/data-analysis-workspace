# KIM_MEASURE_TYPE_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view by selecting all columns from the 'KIM_MEASURE_TYPE_DIM' table. It applies NULL value handling (replacing NULLs with -1) and type casting to 'MEASURE_TYPE_NAME' and 'MEASURE_TYPE_DESC' columns.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_MEASURE_TYPE_DIM]]
| Column Name |
|---|
| MEASURE_TYPE_KEY |
| MEASURE_TYPE_NAME |
| MEASURE_TYPE_DESC |



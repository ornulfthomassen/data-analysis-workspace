# KIM_SALGSTAVLE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a curated set of customer communication and campaign response data. It directly selects most columns from its source table and applies a specific transformation to the 'MAIN_NUMBER' column: if 'MAIN_NUMBER' is null or less than 1, it is set to NULL, otherwise its original value is retained. This suggests a data cleaning or normalization step for this specific identifier, likely preparing the data for reporting or analytical dashboards related to sales or campaign performance.

## Data Sources (Inputs)
- ← [[KIM_SALGSTAVLE_T]]


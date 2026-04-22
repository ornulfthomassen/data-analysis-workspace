# KIM_SOURCE_SYSTEM_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view named `KIM_SOURCE_SYSTEM_DIM_V` in the `CRM_ANALYSE` schema. This view serves as a direct pass-through, selecting all columns (`SOURCE_SYSTEM_KEY`, `SOURCE_SYSTEM_NAME`, `SOURCE_SYSTEM_DESC`) from the `SOURCE_SYSTEM_DIM_V` view located in the `galaxy` schema. Its purpose is to expose source system dimension data, potentially for organizational or access control reasons within a different schema context.

## Data Sources (Inputs)
- ← [[galaxy.SOURCE_SYSTEM_DIM_V]]


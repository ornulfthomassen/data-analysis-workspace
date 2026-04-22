# PRODUCT_DIM_VA

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`PRODUCT_DIM_VA`) acts as a prepared product dimension for analytical purposes. It selects a comprehensive set of product attributes, standardizing data types (primarily casting to VARCHAR2 with specified lengths) and handling NULL values by replacing them with a default placeholder ('-1') for most columns. This ensures data consistency and readiness for downstream reporting or analytical processes, effectively serving as a data transformation layer for product master data.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]


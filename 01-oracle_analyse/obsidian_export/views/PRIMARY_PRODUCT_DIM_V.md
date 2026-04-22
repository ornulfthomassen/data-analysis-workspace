# PRIMARY_PRODUCT_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named PRIMARY_PRODUCT_DIM_V, serves as a dimension table for primary product information. It selects a comprehensive set of product attributes, including names, descriptions, types, brands, various DRM (Digital Rights Management or Data Reference Model) classifications, pricing details, dates, and service-specific features (e.g., included data/minutes). The view filters the base product dimension to include only products marked with specific 'PRIMARY_PRODUCT_FLAG' values (1, -1, or -2), effectively presenting a subset of products considered 'primary' for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]


# PRODUCT_DIM_MOB_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named PRODUCT_DIM_MOB_V, extracts various product dimension attributes (such as product area, technology, category, group, brand, reporting, portfolio, service, payment, rank, and income service) from the 'galaxy.product_dim' table. Its primary function is to standardize these attributes by explicitly casting them to fixed-length CHAR data types, likely for specific reporting purposes, external system integration, or consumption by applications (e.g., mobile applications, indicated by 'MOB' in the view name) that require consistent data types.

## Data Sources (Inputs)
- ← [[galaxy.product_dim]]


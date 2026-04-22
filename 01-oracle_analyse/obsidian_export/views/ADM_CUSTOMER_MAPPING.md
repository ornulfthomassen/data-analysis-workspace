# ADM_CUSTOMER_MAPPING

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view serves as a direct alias or wrapper for the `ccdw.customer_mapping` table. It exposes all columns from the underlying table without any transformations, aggregations, or filtering. Its purpose is likely to provide a simplified name, schema separation for access control (e.g., granting permissions on `ADM_CUSTOMER_MAPPING` instead of `CCDW.CUSTOMER_MAPPING`), or to facilitate migration/refactoring by abstracting the actual table name.

## Data Sources (Inputs)
- ← [[CCDW.CUSTOMER_MAPPING]]


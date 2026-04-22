# DIMPOSTNUMMER

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and consolidates postal code information by administrative region (county and municipality). For each unique combination of county code, county name, municipality code, and municipality name, it selects the numerically smallest postal code and its corresponding latitude, longitude, and postal place. This effectively provides a representative or primary postal code for each administrative region.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]


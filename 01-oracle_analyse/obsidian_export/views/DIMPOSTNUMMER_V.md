# DIMPOSTNUMMER_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates postal code data by county (FYLKEKODE, FYLKE) and municipality (KOMMUNEKODE, KOMMUNE). For each unique combination of county and municipality, it selects the lowest postal code (POSTNUMMER) and its associated latitude, longitude, and poststed. This effectively creates a summarized geographical dimension table where each row represents a unique municipality/county, using a specific postal code as its identifier and representative geographical point.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]


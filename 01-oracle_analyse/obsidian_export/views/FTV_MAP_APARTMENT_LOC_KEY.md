# FTV_MAP_APARTMENT_LOC_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
This view maps various location identifiers to a determined 'CURRENT_APARTMENT_LOC_KEY'. It prioritizes assigning a unique 'CURRENT_APARTMENT_LOC_KEY' for 'CURRENT_STREET_LOC_KEY's that are associated with exactly one current apartment. For all other apartment locations, it uses their own 'CURRENT_GEOGRAPHY_ID' as the 'CURRENT_APARTMENT_LOC_KEY'. The view effectively consolidates and standardizes apartment location identifiers based on their street location context.

## Data Sources (Inputs)
- ← [[GALAXY.LOCATION_DIM]]


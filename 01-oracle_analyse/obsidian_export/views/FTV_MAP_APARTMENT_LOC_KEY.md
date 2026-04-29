# FTV_MAP_APARTMENT_LOC_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `FTV_MAP_APARTMENT_LOC_KEY`, provides a consolidated mapping for apartment location keys and their associated street location keys. It derives `CURRENT_STREET_LOC_KEY` from `CURRENT_GEOGRAPHY_ID_HOUSE` and sets `CURRENT_APARTMENT_LOC_KEY` by either prioritizing a unique 'current' apartment's `CURRENT_GEOGRAPHY_ID` at a given street/house level (if such a unique current apartment exists), or by using the apartment's own `CURRENT_GEOGRAPHY_ID` otherwise. It also includes the original `LOCATION_KEY`, `IS_CURRENT`, and `IS_APARTMENT` flags.

## Data Sources (Inputs)
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| IS_CURRENT |
| IS_APARTMENT |
| CURRENT_GEOGRAPHY_ID_HOUSE |
| CURRENT_GEOGRAPHY_ID |


# DIMPOSTNUMMER

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates postal code dimension data from a base table. For each unique combination of 'Fylke' (county) and 'Kommune' (municipality) codes and names, it selects the postal code, latitude, longitude, and poststed (postal place) that corresponds to the lowest postal code within that group.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
| Column Name |
|---|
| POSTNUMMER |
| LATITUDE |
| LONGITUDE |
| POSTSTED |
| FYLKEKODE |
| FYLKE |
| KOMMUNEKODE |
| KOMMUNE |


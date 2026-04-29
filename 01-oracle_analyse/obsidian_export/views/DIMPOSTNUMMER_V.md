# DIMPOSTNUMMER_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates postal code information by Fylke (county) and Kommune (municipality), selecting the lowest postal code and its corresponding latitude, longitude, and poststed (postal town) for each unique administrative region combination.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]
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


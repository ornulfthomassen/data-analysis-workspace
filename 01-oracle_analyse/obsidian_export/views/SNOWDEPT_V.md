# SNOWDEPT_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines postal code and geographical information (latitude, longitude, county, municipality) from the DIMPOSTNUMMER table with snow depth and location details from the SNOWDEPTH table. The join is performed based on normalized (uppercased) county and municipality names to link geographical data with snow depth observations.

## Data Sources (Inputs)
- ← [[SNOWDEPTH]]
| Column Name |
|---|
| STED |
| SNOW |
| FYLKE |
| KOMMUNE |
- ← [[DIMPOSTNUMMER]]
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


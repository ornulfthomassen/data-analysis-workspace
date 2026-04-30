# KIM_POSTCODE_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view for Norwegian postcode and municipality data, combining and enriching postcode information with municipality-level geographical coordinates from two related dimension tables.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
| Column Name |
|---|
| POSTNUMMER |
| POSTSTED |
| FYLKEKODE |
| FYLKE |
| KOMMUNEKODE |
| KOMMUNE |
| POSTNUMMERKATEGORIKODE |
| POSTNUMMERKATEGORI |
| LATITUDE |
| LONGITUDE |

- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]
| Column Name |
|---|
| KOMMUNEKODE |
| LATITUDE |
| LONGITUDE |



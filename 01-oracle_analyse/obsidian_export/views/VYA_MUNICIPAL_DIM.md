# VYA_MUNICIPAL_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`VYA_MUNICIPAL_DIM`) serves as a comprehensive dimension for municipal, county, and region data, consolidating both current and historical records. It provides detailed geographical information, handling changes over time (Slowly Changing Dimension Type 2) by combining currently valid entries with historical entries linked to their corresponding current municipality.

## Data Sources (Inputs)
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]
| Column Name |
|---|
| MUNICIPALITY_CODE |
| MUNICIPALITY_NAME |
| SUB_COUNTY_CODE |
| SUB_COUNTY_NAME |
| COUNTY_CODE |
| COUNTY_NAME |
| KOMMUNEKATEGORI |
| REGION_CODE |
| REGION_NAME |
| SUB_REGION_CODE |
| SUB_REGION_NAME |
| VALIDFROM |
| VALIDTO |
| MUNICIPALITY_CODE_CURRENT |


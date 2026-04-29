# GCP_MUNICIPALITY_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view, GCP_MUNICIPALITY_DIM, serves as a dimension table that directly exposes all columns from the CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM table. Its primary purpose is to provide municipality-related data, likely for data warehousing or reporting, under a different schema and view name without any transformations or filtering.

## Data Sources (Inputs)
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]
| Column Name |
|---|
| MUNICIPALITY_CODE |
| MUNICIPALITY_CODE_RYDDET_TIL |
| MUNICIPALITY_CODE_CURRENT |
| MUNICIPALITY_NAME |
| SUB_COUNTY_CODE |
| SUB_COUNTY_NAME |
| COUNTY_CODE |
| COUNTY_NAME |
| SUB_REGION_CODE |
| SUB_REGION_NAME |
| REGION_CODE |
| REGION_NAME |
| VALIDFROM |
| VALIDTO |
| KOMMUNEKATEGORI |
| NOTES |


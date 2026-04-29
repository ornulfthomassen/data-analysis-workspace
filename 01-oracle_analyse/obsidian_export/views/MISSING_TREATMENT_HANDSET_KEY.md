# MISSING_TREATMENT_HANDSET_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
Filters treatments from the 'KIM_TREATMENT_DIM' table to identify records where the 'TREATMENT_CD' contains '_TT_' and the 'HANDSET_KEY' is either NULL or -1, effectively pinpointing treatments with a missing or invalid handset key.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_SK |
| TREATMENT_CD |
| TREATMENT_NM |
| TREATMENT_DESC |
| TREATMENT_PRODUCT_KEY |
| TREATMENT_PRODUCT_DESC |
| BRAND |
| KPI_TYPE |
| ACTION_CATEGORY |
| ACTION_CATEGORY_TYPE |
| OFFER_CATEGORY |
| CURRENT_VERSION_FLG |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
| PRODUCT_KEY_5 |
| PRODUCT_KEY_6 |
| START_DATE |
| END_DATE |
| CURRENT_STATUS |
| HANDSET_KEY |


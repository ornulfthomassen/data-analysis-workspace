# ADM_HANDSET_DIM_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
The view `ADM_HANDSET_DIM_V` creates a standardized and enriched dimension table for mobile handsets. It processes raw device data from `CCDW.HANDSET_TYPE_EXT` by applying complex logic to normalize manufacturer names and derive a primary marketing name (`MARKETING_NAME_L1`) from various designation fields. It also generates a secondary marketing name (`MARKETING_NAME_L2`) for unclassified devices, retaining original source values for auditing and debugging purposes. It leverages `ADM_GSMA_MARKETING_NAME_DIM` for lookup and filtering during the data processing.

## Data Sources (Inputs)
- ← [[CCDW.HANDSET_TYPE_EXT]]
| Column Name |
|---|
| TACFAC |
| MODELID |
| HAT_PRODUCER |
| HAT_MODEL_MARKETING_NAME |
| GSMA_NAME |
- ← [[ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| TAC |
| MARKETING_NAME_L1 |


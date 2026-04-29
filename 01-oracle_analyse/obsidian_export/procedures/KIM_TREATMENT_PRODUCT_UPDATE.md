# KIM_TREATMENT_PRODUCT_UPDATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates product key columns (PRODUCT_KEY_1 to PRODUCT_KEY_4) in the `CRM_ANALYSE.KIM_TREATMENT_DIM` table for records where these keys are initially negative. The procedure iterates through four distinct scenarios, each corresponding to one product key column. For each scenario, it identifies `treatment_key` and a new `product_ID` by joining `CRM_ANALYSE.KIM_TREATMENT_DIM` with `RTDM_CDM.CI_TREATMENT`, `RTDM_CDM.CI_TREATMENT_EXT`, and `CLM_CCM.CCM_PRODUCT_TYPE_CONFIG` tables, and then updates the respective `PRODUCT_KEY_N` column.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| treatment_key |
| TREATMENT_CD |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |
- ← [[RTDM_CDM.CI_TREATMENT]]
| Column Name |
|---|
| TREATMENT_CD |
| CURRENT_VERSION_FLG |
| treatment_sk |
- ← [[RTDM_CDM.CI_TREATMENT_EXT]]
| Column Name |
|---|
| treatment_sk |
| PRODUCT_ID1 |
| PRODUCT_ID2 |
| PRODUCT_ID3 |
| PRODUCT_ID4 |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| VALUE |
| SUBSTITUTION_PROD_ID1 |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_KEY_3 |
| PRODUCT_KEY_4 |


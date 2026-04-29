# KIM_UPD_MAIN_NR

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in `crm_analyse.KIM_CAMPAIGN_DETAIL_FACT` that have a null `main_number` and a recent `contact_date_key`. For each matching record, it looks up a `REGARDING_MSISDN` value from `CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG` based on a `TREATMENT_HASH_VAL` join, processes it with `make_number`, and then updates the `main_number` column in `crm_analyse.KIM_CAMPAIGN_DETAIL_FACT` for that record.

## Data Sources (Inputs)
- ← [[crm_analyse.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| TREATMENT_HASH_VAL |
| main_number |
| contact_date_key |
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG]]
| Column Name |
|---|
| REGARDING_MSISDN |
| TREATMENT_HASH_VAL |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| main_number |


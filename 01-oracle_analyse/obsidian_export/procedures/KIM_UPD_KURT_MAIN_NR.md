# KIM_UPD_KURT_MAIN_NR

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates specific identifier fields and a main number in the 'KIM_CAMPAIGN_DETAIL_FACT' table based on corresponding data from the 'KIM_CAMPAIGN_DETAIL_FACT_old' table. It processes records within a specified contact date key range. The update is conditional: if the source value is positive, it updates the target column; otherwise, it retains the existing value. It also stamps updated records with a fixed 'seq_id_upd' value.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_old]]
| Column Name |
|---|
| contact_key |
| KURT_ID_OWNER |
| KURT_ID_PAYER |
| KURT_ID_USER |
| MAIN_NUMBER |
| CONTACT_DATE_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KURT_ID_OWNER |
| KURT_ID_PAYER |
| KURT_ID_USER |
| MAIN_NUMBER |
| seq_id_upd |


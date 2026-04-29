# KIM_UPD_WHATEVER

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through records in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table that match specific criteria (`EFFECT_TYPE = 'FAMILIEBONUS'` and `CONTACT_DATE_KEY >= 20170601`). For each matching record, it updates five columns (`effect_rank`, `effect_date_key`, `EFFECT_TYPE`, `EFFECT_STATUS`, and `seq_id_upd`) by setting the first four to `NULL` and `seq_id_upd` to a fixed value (88888888). Changes are committed periodically after every 100,000 updates.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| contact_key |
| EFFECT_TYPE |
| CONTACT_DATE_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| effect_rank |
| effect_date_key |
| EFFECT_TYPE |
| EFFECT_STATUS |
| seq_id_upd |


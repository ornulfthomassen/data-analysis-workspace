# KIM_MITTTELENOR_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through specific campaign detail records based on a sequence ID, then updates the same records by setting 'EFFECT_DATE_KEY', 'EFFECT_STATUS', 'EFFECT_TYPE', and 'seq_id_upd' columns to NULL. The procedure commits changes in batches of 20,000 records.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| contact_key |
| seq_id_upd |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| EFFECT_DATE_KEY |
| EFFECT_STATUS |
| EFFECT_TYPE |
| seq_id_upd |


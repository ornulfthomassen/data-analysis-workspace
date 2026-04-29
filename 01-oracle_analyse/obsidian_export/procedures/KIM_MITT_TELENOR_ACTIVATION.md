# KIM_MITT_TELENOR_ACTIVATION

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies 'Mitt Telenor' and 'Mitt Djuice' campaign activations by correlating campaign contact details with app usage data, calculates effect rank, date, type, and status, and updates the `KIM_CAMPAIGN_DETAIL_FACT` table accordingly. It also logs the procedure's execution status (start, completion) in the `GOV_DQ_MARTS` table.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| contact_key |
| kurt_id_owner |
| CONTACT_DATE_KEY |
| campaign_key |
| contact_dttm |
| SOURCE_SYSTEM_KEY |
| effect_type |
- ← [[kim_campaign_dim]]
| Column Name |
|---|
| campaign_key |
| campaign_nm |
| CAMPAIGN_CD |
- ← [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION]]
| Column Name |
|---|
| APP_LAST_USED_DATE |
| kurt_id |
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| effect_rank |
| effect_date_key |
| EFFECT_TYPE |
| EFFECT_STATUS |
| seq_id_upd |


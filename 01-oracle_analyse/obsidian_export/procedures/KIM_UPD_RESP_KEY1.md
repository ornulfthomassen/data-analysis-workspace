# KIM_UPD_RESP_KEY1

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates 'effect' related attributes (date key, type, and status) based on campaign data and customer channel interaction app usage for specific campaigns (containing 'MITT TELENOR' or 'MITT DJUICE' in their names). It then updates these calculated values in the campaign detail fact table.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| contact_key |
| campaign_key |
| contact_dttm |
| kurt_id_owner |
| SOURCE_SYSTEM_KEY |
| contact_date_key |
- ← [[kim_campaign_dim]]
| Column Name |
|---|
| campaign_key |
| campaign_nm |
- ← [[CLM_CCM.CCM_CUST_CHANNEL_INTERACTION]]
| Column Name |
|---|
| APP_LAST_USED_DATE |
| kurt_id |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| EFFECT_DATE_KEY |
| EFFECT_TYPE |
| EFFECT_STATUS |
| seq_id_upd |


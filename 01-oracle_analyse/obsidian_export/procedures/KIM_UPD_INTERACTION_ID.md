# KIM_UPD_INTERACTION_ID

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates the `INTERACTION_ID` column in the `KIM_CAMPAIGN_DETAIL_FACT` table. For each `CONTACT_KEY` in `KIM_CAMPAIGN_DETAIL_FACT` that matches specific date and system criteria, the procedure determines the `INTERACTION_ID` from related `KS_INTERACTION` records. The `INTERACTION_ID` is selected as the one with the highest `technical_result` and `end_cal_dt` among `ks_interaction` records whose `start_cal_date` falls within 10 days of the `kim_campaign_detail_fact`'s `contact_dttm` and meet other conditions. Updates are applied in batches and committed periodically.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| CONTACT_KEY |
| MAIN_NUMBER |
| CONTACT_DTTM |
| CONTACT_DATE_KEY |
| SOURCE_SYSTEM_KEY |
- ← [[ks_interaction]]
| Column Name |
|---|
| INTERACTION_ID |
| TECHNICAL_RESULT |
| END_CAL_DT |
| KEYED_NUMBER_NUM |
| CALL_FROM_NUM |
| HANDLE_COUNT |
| START_CAL_DATE |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| INTERACTION_ID |


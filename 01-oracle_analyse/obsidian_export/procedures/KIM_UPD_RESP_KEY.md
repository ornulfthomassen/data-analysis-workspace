# KIM_UPD_RESP_KEY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure identifies records in `kim_campaign_detail_fact` that have a `RESPONSE_KEY` of -1, a `contact_date_key` on or after 20180627, and an associated `TRIGGER_ID` in `kim_campaign_detail_fact_ext`. For each identified record, it updates the `RESPONSE_KEY` to 71 in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table. The updates are committed in batches of 100,000 records.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| CONTACT_KEY |
| contact_date_key |
| RESPONSE_KEY |
- ← [[kim_campaign_detail_fact_ext]]
| Column Name |
|---|
| CONTACT_KEY |
| TRIGGER_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| RESPONSE_KEY |


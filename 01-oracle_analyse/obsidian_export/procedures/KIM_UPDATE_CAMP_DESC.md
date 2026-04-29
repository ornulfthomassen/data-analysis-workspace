# KIM_UPDATE_CAMP_DESC

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure identifies specific campaign detail records based on a combination of campaign details, campaign extensions, and campaign dimension attributes. For each identified record, it updates the `ORDER_RANK` to NULL and sets the `campaign_type_desc` to 'Treatment' in the `KIM_CAMPAIGN_DETAIL_FACT` table. It commits changes in batches of 100,000 records.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| contact_key |
| CAMPAIGN_KEY |
| contact_date_key |
| campaign_type_desc |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| contact_key |
| trigger_id |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| campaign_type_desc |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_RANK |
| campaign_type_desc |


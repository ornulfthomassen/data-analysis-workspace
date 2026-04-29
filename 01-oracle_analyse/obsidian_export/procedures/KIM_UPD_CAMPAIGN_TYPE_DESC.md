# KIM_UPD_CAMPAIGN_TYPE_DESC

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates the 'campaign_type_desc' column in the 'KIM_CAMPAIGN_DETAIL_FACT' table for records where this column is currently NULL. It determines the new description by joining with 'KIM_CAMPAIGN_DIM' and applying a CASE statement based on 'CAMPAIGN_TYPE_CD'. The updates are committed in batches of 1000 records.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| CONTACT_KEY |
| campaign_type_desc |
| CAMPAIGN_KEY |
- ← [[kim_campaign_dim]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| CAMPAIGN_TYPE_CD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| campaign_type_desc |


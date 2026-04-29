# KIM_CAMPAIGN_GROUP_FIX

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates the 'CAMPAIGN_GROUP_SK' column in the `CRM_ANALYSE.KIM_CAMPAIGN_DIM` table. It identifies records where `CAMPAIGN_GROUP_SK` is negative but a corresponding positive `CAMPAIGN_GROUP_SK` exists for the same `CAMPAIGN_CD` within the `KIM_CAMPAIGN_DIM` table (joined with `KIM_CAMPAIGN_GROUP_DIM`). It then updates the negative `CAMPAIGN_GROUP_SK` with the valid positive one. The updates are committed in batches of 10,000 records.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| CAMPAIGN_CD |
| CAMPAIGN_GROUP_SK |
- ← [[KIM_CAMPAIGN_GROUP_DIM]]
| Column Name |
|---|
| CAMPAIGN_GROUP_SK |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_GROUP_SK |
| CAMPAIGN_KEY |
| CAMPAIGN_CD |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_GROUP_SK |


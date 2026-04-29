# KIM_UPD_SMS_RESPONSE_FIX

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through specific records in the 'kim_campaign_detail_fact' table (filtered by join with 'KIM_CHANNEL_DIM' for SMS channels, contact date, source system, and an initial response key of -1) and updates the 'RESPONSE_KEY' to -58 for each matching record in the 'CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT' table, committing changes periodically.

## Data Sources (Inputs)
- ← [[kim_campaign_detail_fact]]
| Column Name |
|---|
| CONTACT_KEY |
| CHANNEL_KEY |
| CONTACT_DATE_KEY |
| SOURCE_SYSTEM_KEY |
| RESPONSE_KEY |
- ← [[KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_KEY |
| CHANNEL_COMMON_NM |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| RESPONSE_KEY |
| CONTACT_KEY |


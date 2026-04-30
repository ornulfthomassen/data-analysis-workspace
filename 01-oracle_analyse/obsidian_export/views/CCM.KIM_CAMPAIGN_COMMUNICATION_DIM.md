# KIM_CAMPAIGN_COMMUNICATION_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines campaign and communication dimension data by joining the KIM_COMMUNICATION_DIM and KIM_CAMPAIGN_DIM tables/views. It creates a unified dimension for campaign communications, deriving a unique key (CAMPAIGN_COMMUNICATION_KEY) by concatenating CAMPAIGN_KEY and COMMUNICATION_KEY, and includes various descriptive attributes for both campaigns and communications.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| CAMPAIGN_SK |
| COMMUNICATION_KEY |
| SOURCE_SYSTEM_KEY |
| COMMUNICATION_CD |
| COMM_PLATFORM |
| ACTIVITY_AREA |
| ACTION_CATEGORY |
| OFFER_CATEGORY |
| OFFER_BRAND |
| COMMUNICATION_NM |
| COMMUNICATION_DESC |

- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| CAMPAIGN_SK |
| SOURCE_SYSTEM_KEY |
| CAMPAIGN_KEY |
| CAMPAIGN_CD |
| CAMPAIGN_NM |
| CAMPAIGN_GROUP_SK |



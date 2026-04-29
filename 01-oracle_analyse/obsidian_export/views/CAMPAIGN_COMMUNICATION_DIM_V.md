# CAMPAIGN_COMMUNICATION_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a dimension view by joining campaign and communication data, providing distinct campaign and communication-related attributes such as action categories, activity areas, campaign codes, communication platforms, and offer details.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DIM]]
| Column Name |
|---|
| ACTIVITY_AREA |
| CAMPAIGN_CD |
| CAMPAIGN_GROUP_SK |
| CAMPAIGN_NM |
| COMM_PLATFORM |
| CAMPAIGN_SK |
| SOURCE_SYSTEM_KEY |
- ← [[KIM_COMMUNICATION_DIM]]
| Column Name |
|---|
| ACTION_CATEGORY |
| COMMUNICATION_CD |
| COMMUNICATION_DESC |
| COMMUNICATION_NM |
| OFFER_BRAND |
| OFFER_CATEGORY |
| SOURCE_SYSTEM_KEY |
| CAMPAIGN_SK |


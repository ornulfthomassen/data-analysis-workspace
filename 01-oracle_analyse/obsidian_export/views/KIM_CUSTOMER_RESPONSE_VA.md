# KIM_CUSTOMER_RESPONSE_VA

**Schema:** `CCM` | **Type:** `View`

## Description
Combines customer response data with descriptive details from response and channel dimensions, and ranks customer responses for analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_CHANNEL_CD |
| RESPONSE_DTTM |
| RESPONSE_CD |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_NM |
| RESPONSE_GROUP |
| RESPONSE_RANK |
| RESPONSE_CD |
| SOURCE_SYSTEM_KEY |
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_NM |
| CHANNEL_COMMON_NM |
| CHANNEL_CD |
| SOURCE_SYSTEM_KEY |


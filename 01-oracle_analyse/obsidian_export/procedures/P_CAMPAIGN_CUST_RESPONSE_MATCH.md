# P_CAMPAIGN_CUST_RESPONSE_MATCH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure processes customer response data to identify and update the most relevant (highest-ranked) response for each contact into a campaign detail fact table. It retrieves unprocessed customer responses, enriches them with dimension data, and for the top-ranked response of each contact, updates the corresponding campaign detail fact record. It then marks the processed customer response record as 'used'. The procedure also manages bitmap indexes on the campaign detail fact table for performance optimization.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| CUST_RESPONSE_KEY |
| RESPONSE_DTTM |
| RESPONSE_CD |
| RESPONSE_CHANNEL_CD |
| USED_FLG |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_KEY |
| RESPONSE_CD |
| SOURCE_SYSTEM_KEY |
| CURRENT_STATUS |
| RESPONSE_RANK |
- ← [[CRM_ANALYSE.KIM_RESPONSE_CHANNEL_DIM]]
| Column Name |
|---|
| RESPONSE_CHANNEL_KEY |
| RESPONSE_CHANNEL_CD |
| SOURCE_SYSTEM_KEY |
| RESPONSE_CD |
| CURRENT_STATUS |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| MEASURE_TYPE |
- → [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| USED_FLG |
| CUST_RESPONSE_KEY |
| SOURCE_SYSTEM_KEY |
| CONTACT_KEY |


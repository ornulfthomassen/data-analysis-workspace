# KIM_RESPONSE_CAMP_MATCH_CLM

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Processes customer response data by identifying the highest-ranked response for each contact. For these top responses, it updates a campaign detail fact table with associated response, date, and channel keys. Concurrently, it marks the original customer response records as 'used'. The procedure also logs its execution status and the number of processed records in a system log table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
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
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_KEY |
- ← [[STLOG.ST_IN]]
| Column Name |
|---|
| RUN_ID |
| SEQ_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |
| SEQ_ID_UPD |
- → [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| USED_FLG |
- → [[STLOG.ST_IN]]
| Column Name |
|---|
| NUM_RECS_IN_TARGET |


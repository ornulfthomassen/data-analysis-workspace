# KIM_IB_CAMP_CUST_RESP_MATCH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Processes customer responses to campaigns. It identifies the primary response for each contact based on predefined ranking logic, updates corresponding campaign detail records with this primary response information, and then marks the processed customer responses as 'used'. The updates are committed in batches of 1000 records.

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
| RESPONSE_RANK |
| RESPONSE_CD |
| SOURCE_SYSTEM_KEY |
| CURRENT_STATUS |
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


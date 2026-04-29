# KIM_RESP_FIX_2

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Identifies primary customer responses based on defined ranking criteria. For each primary response, it updates the corresponding campaign detail fact record with response-related keys and marks the original customer response record as 'used'. The procedure includes transaction management (commits), logging of execution status and record counts, and index statistics gathering.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_CD |
| RESPONSE_DTTM |
| RESPONSE_CHANNEL_CD |
| USED_FLG |
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_CD |
| SOURCE_SYSTEM_KEY |
| CURRENT_STATUS |
| RESPONSE_KEY |
| RESPONSE_RANK |
| RESPONSE_COMMON_NM |
- ← [[CRM_ANALYSE.KIM_RESPONSE_CHANNEL_DIM]]
| Column Name |
|---|
| RESPONSE_CHANNEL_CD |
| SOURCE_SYSTEM_KEY |
| RESPONSE_CD |
| CURRENT_STATUS |
| RESPONSE_CHANNEL_KEY |
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


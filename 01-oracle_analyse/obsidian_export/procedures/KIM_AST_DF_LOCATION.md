# KIM_AST_DF_LOCATION

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure updates the 'CONTACT_LOCATION' column in the 'CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT' table. It iterates through specific customer response records from 'CRM_ANALYSE.KIM_CUSTOMER_RESPONSE' that meet certain criteria (source system, response channel, and related campaign details with a null contact location). For each qualifying record, it derives a 'CONTACT_LOCATION' value by parsing the 'EXTERNAL_RESPONSE_INFO_ID1' field and then updates the corresponding campaign detail fact record where 'CONTACT_LOCATION' is currently null.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| EXTERNAL_RESPONSE_INFO_ID1 |
| SOURCE_SYSTEM_KEY |
| RESPONSE_CHANNEL_CD |
| CUST_RESPONSE_KEY |
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| MEASURE_TYPE |
| SOURCE_SYSTEM_KEY |
| CONTACT_LOCATION |
| CONTACT_KEY |
| CHANNEL_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_LOCATION |


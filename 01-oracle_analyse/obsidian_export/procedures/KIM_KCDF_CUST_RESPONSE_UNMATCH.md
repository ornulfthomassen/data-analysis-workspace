# KIM_KCDF_CUST_RESPONSE_UNMATCH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure resets specific customer response-related key columns to a value of -1 in the 'CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT' table. It processes records within a specified date range (P_YYYYMMDD_FRA to P_YYYYMMDD_TIL) for two distinct source systems (identified by SOURCE_SYSTEM_KEY = 58 and SOURCE_SYSTEM_KEY = 63) where 'CUST_RESPONSE_KEY' is greater than 0. It performs updates in batches with commits.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| CUST_RESPONSE_KEY |
| CONTACT_DTTM |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |


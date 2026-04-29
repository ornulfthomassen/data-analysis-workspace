# KIM_RESET_RESPONSE_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure resets (sets to -1) several response-related key columns (CUST_RESPONSE_KEY, RESPONSE_DATE_KEY, RESPONSE_KEY, RESPONSE_CHANNEL_KEY) in the KIM_CAMPAIGN_DETAIL_FACT table. It operates on records within a specified date range (P_YYYYMMDD_FRA to P_YYYYMMDD_TIL) and only for those records where CUST_RESPONSE_KEY is greater than 0. The updates are performed in batches and committed periodically.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CUST_RESPONSE_KEY |
| CONTACT_DATE_KEY |
| SOURCE_SYSTEM_KEY |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |


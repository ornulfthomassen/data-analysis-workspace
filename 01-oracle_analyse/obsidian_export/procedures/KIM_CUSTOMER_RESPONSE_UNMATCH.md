# KIM_CUSTOMER_RESPONSE_UNMATCH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure processes customer response records from the `CRM_ANALYSE.KIM_CUSTOMER_RESPONSE` table. It identifies records originating from `SOURCE_SYSTEM_KEY` 58 (referred to as 'INBOUND (AST)') and `SOURCE_SYSTEM_KEY` 63 (referred to as 'OUTBOUND (CI)') within a specified date range (`P_YYYYMMDD_FRA` to `P_YYYYMMDD_TIL`) and where `CONTACT_KEY` is positive. For each identified record, it updates the `CONTACT_KEY` to -1 and `USED_FLG` to 0, effectively 'unmatching' or invalidating these customer responses in batches of 100,000 records.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| SOURCE_SYSTEM_KEY |
| CONTACT_KEY |
| RESPONSE_DTTM |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| USED_FLG |
| CUST_RESPONSE_KEY |
| SOURCE_SYSTEM_KEY |


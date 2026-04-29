# KIM_RESPONSE_BLANK_AST_OLD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in KIM_CAMPAIGN_DETAIL_FACT based on specific criteria (date, measure type, source system, customer response key) and updates several 'response' related columns and CUST_RESPONSE_KEY to -1 for each matching record. The updates are performed in batches with periodic commits.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DATE_KEY |
| MEASURE_TYPE |
| SOURCE_SYSTEM_KEY |
| CUST_RESPONSE_KEY |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |
| RESPONSE_REASON_KEY |
| CUST_RESPONSE_KEY |


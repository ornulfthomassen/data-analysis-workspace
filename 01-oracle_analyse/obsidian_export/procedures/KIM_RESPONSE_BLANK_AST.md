# KIM_RESPONSE_BLANK_AST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through specific records in the KIM_CAMPAIGN_DETAIL_FACT table, identified by criteria including contact date, measure type, source system, and customer response key. For each identified record, it updates several response-related columns (RESPONSE_DATE_KEY, RESPONSE_KEY, RESPONSE_CHANNEL_KEY, RESPONSE_REASON_KEY, CUST_RESPONSE_KEY) to a value of -1, effectively 'blanking out' or resetting these response details. Commits are performed periodically (every 10,000 records) and at the end of the procedure.

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


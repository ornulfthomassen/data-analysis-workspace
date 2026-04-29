# KIM_RESPONSE_MATCH_CLM

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure identifies customer responses that have not yet been marked as 'used' (USED_FLG = 0) and attempts to link them to the most recent relevant customer contact. It determines a date range based on these responses and then, for each eligible customer response, finds the latest contact (from KIM_CAMPAIGN_DETAIL_FACT) that matches certain criteria (customer ID, cell package, source system, treatment, and occurred before the response within the calculated date range). The CONTACT_KEY from this matched contact is then updated back into the KIM_CUSTOMER_RESPONSE table, along with setting RESPONSE_VALUE_AMT to 1, for the corresponding customer response records. The updates are performed in batches with commit operations.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| RESPONSE_DATE |
| USED_FLG |
| RESPONSE_DATE_KEY |
| CUST_RESPONSE_KEY |
| SOURCE_SYSTEM_KEY |
| TREATMENT_SK |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
| RESPONSE_DTTM |
- ← [[KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_SK |
| TREATMENT_KEY |
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| CONTACT_DTTM |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
| CONTACT_DATE_KEY |
| TREATMENT_KEY |
| SOURCE_SYSTEM_KEY |

## Target Tables (Outputs)
- → [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_VALUE_AMT |


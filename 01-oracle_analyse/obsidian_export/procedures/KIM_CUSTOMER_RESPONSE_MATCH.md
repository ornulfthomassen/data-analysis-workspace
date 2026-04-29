# KIM_CUSTOMER_RESPONSE_MATCH

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Matches customer responses to campaign contacts based on defined criteria across two source systems (63 and 58). It updates the contact key and response value amount in the customer response record, logging the procedure's execution status and details in a governance data quality mart.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| TREATMENT_SK |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
| SOURCE_SYSTEM_KEY |
| CONTACT_KEY |
| CUST_RESPONSE_KEY |
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
| SOURCE_SYSTEM_KEY |
| MEASURE_TYPE |
| TREATMENT_KEY |
- ← [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| RUNTIME |

## Target Tables (Outputs)
- → [[CLM_CCM.GOV_DQ_MARTS]]
| Column Name |
|---|
| RUNTIME |
| FREQ |
| SYSTEM_NM |
| PROCESS_NM |
| STATUS_NM |
| REASON |
| PRIORITY |
| START_TIME |
| END_TIME |
| PREV_OK_DTTM |
| PREV_OK_RESSULT |
| LAST_RESSULT |
- → [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| RESPONSE_VALUE_AMT |


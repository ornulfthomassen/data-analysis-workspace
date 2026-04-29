# KIM_CUSTOMER_RESPONSE_MATCH_94

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Matches customer responses to contact keys from campaign detail facts based on specific criteria (e.g., campaign type, response time windows). It updates the `CRM_ANALYSE.KIM_CUSTOMER_RESPONSE` table with the newly matched `CONTACT_KEY` and a `RESPONSE_VALUE_AMT`. The procedure also logs its execution status and timestamps in the `CLM_CCM.GOV_DQ_MARTS` table.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| TREATMENT_SK |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
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
| CAMPAIGN_TYPE_DESC |
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


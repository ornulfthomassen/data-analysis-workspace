# KIM_CUSTOMER_RESP_MATCH_94

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure identifies customer responses that are not yet linked to a contact (where `CONTACT_KEY = -1`). It attempts to match these responses to existing campaign contacts based on specific criteria involving campaign type, source system, and response timing. Upon successful matching, it updates the `CONTACT_KEY` and assigns a `RESPONSE_VALUE_AMT` (either 1 or 2) in the `CRM_ANALYSE.KIM_CUSTOMER_RESPONSE` table. The procedure also logs its execution status, including start and end times, into the `CLM_CCM.GOV_DQ_MARTS` table and gathers statistics on a relevant index.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| TREATMENT_SK |
| KURT_ID_OWNER |
| CELL_PACKAGE_SK |
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


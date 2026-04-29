# KIM_KS_IVR_DIALOG_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines IVR (Interactive Voice Response) dialog data with customer mapping details and customer satisfaction (CSAT) survey responses. It enriches the IVR interaction data with time-based dimensions (date, month, week), maps owner and user IDs to customer keys, and adjusts service names/types for reporting, while also incorporating CSAT scores for specific questions.

## Data Sources (Inputs)
- ← [[RSSHUGIN.IVR_DIALOG]]
| Column Name |
|---|
| START_TIME |
| CONN_ID |
| SERVICE_PATH |
| CALLED_SERVICE |
| B_NUMBER |
| KURT_ID_OWNER |
| KURT_ID_USER |
| IVR_SERVICE_ID |
| VIRTUAL_QUEUE |
| TECHNICAL_RESULT |
| RESULT_REASON |
| CUSTOMER_HANDLE_COUNT |
| SERVICE_NAME |
| SERVICE_TYPE |
| PRECEDING_SERVICE |
| NEXT_SERVICE |
| OFFERED_SERVICES |
| STEP_ORDER |
| S_START_TIME |
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]
| Column Name |
|---|
| transaction_id |
| QUESTION_NAME |
| ANSWER_ID |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |


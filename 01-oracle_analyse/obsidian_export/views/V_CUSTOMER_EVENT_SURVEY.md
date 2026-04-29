# V_CUSTOMER_EVENT_SURVEY

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view (`V_CUSTOMER_EVENT_SURVEY`) consolidates detailed information about a specific customer event survey (identified by `SURVEY_ID = 336`). It joins survey metadata, individual questions, and corresponding customer responses to provide a comprehensive dataset including survey name, question text, response scores, answer details, invitation and response timestamps, customer type, journey description, source system information, and product/device details.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.SURVEYS]]
| Column Name |
|---|
| SURVEY_ID |
| SURVEY_NAME |
- ← [[CCDW_CUSTOMER_EVENT.QUESTIONS]]
| Column Name |
|---|
| QUESTION_ID |
| QUESTION_TEXT |
| SURVEY_ID |
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]
| Column Name |
|---|
| RESPONSE_ID |
| SOURCE_SYSTEM_ID |
| ANSWER_ID |
| ANSWER_TEXT |
| STARTDATE |
| ENDDATE |
| CUSTOMER_TYPE |
| CUSTOMER_JOURNEY_DESC |
| SOURCE_SYSTEM_DESC |
| SUBSCRIPTION_ID |
| POSTCODE |
| POST_NAME |
| AREA |
| PRODUCT_NAME |
| FINISHED |
| DEVICE_MODEL_ID |
| DEVICE_MODEL_NAME |
| QUESTION_ID |


# CCDW_CTI_QUALTRICS_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines survey response data from 'SURVEY_RESPONSE_FACT' with question details from 'QUESTIONS', filtering for 'NO_TRANSACTION_CALL_CENTER' customer journeys to provide a unified view of Qualtrics survey interactions.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]
| Column Name |
|---|
| STARTDATE |
| ENDDATE |
| SENTFROMCHANNELDATE |
| TRANSACTION_START_DT |
| TRANSACTION_ID |
| BRAND_NAME |
| CHANNEL_TYPE |
| DEPARTMENT_DESC |
| SOURCE_SYSTEM_DESC |
| TRANSFERRED_COUNT |
| FINISHED |
| PRIORITY |
| PRODUCT_CLASS |
| CENTER_NAME |
| QUESTION_NAME |
| ANSWER_TEXT |
| ANSWER_ID |
| QUESTION_ID |
| SURVEY_ID |
| CUSTOMER_JOURNEY_DESC |
- ← [[CCDW_CUSTOMER_EVENT.QUESTIONS]]
| Column Name |
|---|
| QUESTION_TEXT |
| QUESTION_ID |
| SURVEY_ID |


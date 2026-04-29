# VA_SURVEYS

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Consolidates and categorizes Qualtrics survey results, enriching them with customer and device metadata, to provide a comprehensive view of survey responses across different question types. It handles various question types like headings, single-choice with comments, multiple-choice with comments, free-text comments, NPS scores, and SMS comments, filtering data for specific survey IDs.

## Data Sources (Inputs)
- ← [[NPS.SURVEYS]]
| Column Name |
|---|
| NAME |
| SURVEY_ID |
- ← [[NPS.SURVEY_ANSWER_META]]
| Column Name |
|---|
| STARTDATE |
| ENDDATE |
| RECORDED_DATE |
| RESPONSE_ID |
| CUSTOMER_ID |
| CUSTOMER_ID_OWNER |
| CUSTOMER_TYPE |
| CUSTOMER_JOURNEY |
| SUBSCRIPTION_ID |
| AGE |
| AGE_GROUP |
| POSTCODE |
| POST_NAME |
| MUNICIPALITY |
| MUNICIPALITY_ID |
| AREA_NAME |
| AREA |
| DEVICE_MODEL_ID |
| DEVICE_MODEL_NAME |
| DEVICE_PRODUCER_NAME |
| DEVICE_CATEGORY |
| DEVICE_TYPE |
| DEVICE_OS |
| DEVICE_VOLTE_YN |
| DEVICE_LTE_YN |
| DEVICE_HD_VOICE_YN |
| DEVICE_TOUCHSCREEN_YN |
| DEVICE_VOWIFI |
| STATUS |
| RESULT |
| PRODUCT_NAME |
| RESPONSESET |
| FINISHED |
| SOURCE_SYSTEM |
| CONSENT_PROVIDED_YN |
| SURVEY_ID |
- ← [[NPS.SURVEY_QUESTIONS]]
| Column Name |
|---|
| QUESTION_NAME |
| QUESTIONTEXT |
| SURVEY_ID |
| QUESTION_TYPE |
| SUBSELECTOR |
| SELECTOR |
- ← [[NPS.SURVEY_ANSWER]]
| Column Name |
|---|
| SURVEY_ID |
| ANSWER |
| RESPONSE_ID |
| QUESTION |
- ← [[NPS.SURVEY_QUESTION_CHOICES]]
| Column Name |
|---|
| DESCRIPTION |
| SURVEY_ID |
| QUESTION_NAME |
| RECODE |


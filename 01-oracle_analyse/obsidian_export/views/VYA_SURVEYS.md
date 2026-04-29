# VYA_SURVEYS

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and transforms detailed results from various Qualtrics surveys, classifying different question types (e.g., NPS, multiple choice, text comments, headings) and enriching the data with survey metadata, customer demographics, and device information. The view combines data from multiple survey-related tables to provide a comprehensive record of survey responses, tailored to specific survey IDs and answer types.

## Data Sources (Inputs)
- ← [[NPS.SURVEYS]]
| Column Name |
|---|
| SURVEY_ID |
| NAME |
- ← [[NPS.SURVEY_ANSWER_META]]
| Column Name |
|---|
| SURVEY_ID |
| RESPONSE_ID |
| STARTDATE |
| ENDDATE |
| RECORDED_DATE |
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
- ← [[NPS.SURVEY_QUESTIONS]]
| Column Name |
|---|
| SURVEY_ID |
| QUESTION_NAME |
| QUESTIONTEXT |
| QUESTION_TYPE |
| SUBSELECTOR |
| SELECTOR |
- ← [[NPS.SURVEY_ANSWER]]
| Column Name |
|---|
| SURVEY_ID |
| RESPONSE_ID |
| QUESTION |
| ANSWER |
- ← [[NPS.SURVEY_QUESTION_CHOICES]]
| Column Name |
|---|
| SURVEY_ID |
| QUESTION_NAME |
| RECODE |
| DESCRIPTION |


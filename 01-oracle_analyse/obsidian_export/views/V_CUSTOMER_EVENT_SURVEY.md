# V_CUSTOMER_EVENT_SURVEY

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view provides detailed information for a specific customer event survey (SURVEY_ID = 336), combining survey metadata, question details, and response data. It includes information such as survey name, question text, response score/answer, invitation and response timestamps, customer type, journey description, source system details, and other demographic/product-related information from the survey responses.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.SURVEYS]]
- ← [[CCDW_CUSTOMER_EVENT.QUESTIONS]]
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]


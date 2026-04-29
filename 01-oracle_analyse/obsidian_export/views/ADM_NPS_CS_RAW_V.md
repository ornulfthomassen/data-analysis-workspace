# ADM_NPS_CS_RAW_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view combines Net Promoter Score (NPS) survey data from the Medallia import table with customer mobile subscription history and mobile number porting information. It cleans and standardizes raw NPS scores, deriving a calculated NPS value and categorizing it. The view enriches the data with various customer and call attributes, as well as porting status details, to provide a comprehensive dataset for detailed NPS analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
| LAST_DATE_KEY |
| FIRST_DATE_KEY |
- ← [[NPS.MEDALLIA_SURVEY_IMPORT]]
| Column Name |
|---|
| PHONE_NUMBER |
| CUSTOMER_ID_OWNER |
| CUSTOMER_ID_USER |
| INPUT_NUMBER |
| TELENOR_UNIQUE_ID |
| TRANSACTION_DATE |
| SURVEY_SENT_TIME |
| RESPONSE_DATE |
| TOPIC_OF_CALL |
| CONSUMER_DIVISION |
| MOBILE_BRAND |
| REPEATED_CALL |
| TRANSFERRED_CALL |
| TIME_IN_QUEUE |
| CONVERSATION_TIME |
| CUSTOMER_TYPE |
| AGE_GROUP |
| DISTRICT |
| PORTFOLIO |
| LIKELIHOOD_TO_CHURN |
| CONTACT_CENTER |
| UNIT |
| LIKELIHOOD_TO_RECOMMEND |
| LIKELIHOOD_TO_RECOMMEND_RAW |
| NPS_CATEGORY |
| REASON_FOR_SCORE_RAW |
| RESCUED |
| AVOIDED_CHURN |
| SALE |
| SURVEY_PROGRAM |
| COMPLETED_WEB_SURVEY |
| REASON_COMMENT_PROVIDED |
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| SUBSCR_ID |
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_PHONE_NUM |
| ORDER_STATUS_ID |
| ORDER_ARRIVAL_DATE |
| INFO_CHG_DATE |
| SERVICE_PROVIDER_ID_OUT |
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
| Column Name |
|---|
| ORDER_ID |
| SUBSCR_ID |


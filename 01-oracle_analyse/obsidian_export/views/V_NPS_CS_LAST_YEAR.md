# V_NPS_CS_LAST_YEAR

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view provides a historical overview of Net Promoter Score (NPS) survey data from the past 12 months. It enriches the survey data by linking it to mobile subscription history records for both the caller and input phone numbers, capturing details like subscription ID, owner, and user. The view standardizes NPS categories, calculates days since the transaction, and ranks surveys for each customer/user based on transaction recency.

## Data Sources (Inputs)
- ← [[NPS.MEDALLIA_SURVEY_IMPORT]]
| Column Name |
|---|
| TELENOR_UNIQUE_ID |
| TRANSACTION_DATE |
| RESPONSE_DATE |
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
| PHONE_NUMBER |
| INPUT_NUMBER |
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| OWNER |
| FIRST_USER |
| START_DATE |
| END_DATE |


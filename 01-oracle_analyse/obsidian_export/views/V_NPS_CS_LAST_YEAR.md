# V_NPS_CS_LAST_YEAR

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view provides enriched Net Promoter Score (NPS) survey data for Customer Service from the last 12 months. It calculates NPS categories and scores, determines the days since each transaction, and associates caller and input subscriber details (main number, subscription ID, owner, user ID) by joining with mobile subscription history. Additionally, it ranks the surveys for each customer based on the transaction date.

## Data Sources (Inputs)
- ← [[NPS.MEDALLIA_SURVEY_IMPORT]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]


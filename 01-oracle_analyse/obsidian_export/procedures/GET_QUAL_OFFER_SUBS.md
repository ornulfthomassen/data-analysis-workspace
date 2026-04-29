# GET_QUAL_OFFER_SUBS

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Retrieves a treatment key for a given subscription, action category, and campaign date/time. It first identifies the most recent treatment code from the 'ADM_QUAL_OFFER_HIST_SUBSCR' table based on the input parameters. If a treatment code is found, it then uses this code to find the most recent treatment key from the 'KIM_TREATMENT_DIM' table. The function returns the found treatment key, or specific error codes (-1 or -2) if data is not found in either step.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
| Column Name |
|---|
| TREATMENT_CD |
| START_DATE |
| SUBSCRIPTION_ID |
| ACTION_CATEGORY |
| END_DATE |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| START_DATE |
| TREATMENT_CD |


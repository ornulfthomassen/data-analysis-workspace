# GET_QUAL_OFFER_KURT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This function retrieves a 'treatment key' based on a 'Kurt ID', 'action category', and campaign date/time. It first looks up a 'treatment code' from offer history, then uses that code to find the corresponding 'treatment key' from a treatment dimension table, considering date ranges and priorities. It returns the treatment key, or specific error codes (-1 or -2) if not found.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
| Column Name |
|---|
| TREATMENT_CD |
| OWNER_KURT_ID |
| ACTION_CATEGORY |
| CAMP_OFFER_PRIORITY |
| START_DATE |
| END_DATE |
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
| Column Name |
|---|
| TREATMENT_KEY |
| TREATMENT_CD |
| START_DATE |


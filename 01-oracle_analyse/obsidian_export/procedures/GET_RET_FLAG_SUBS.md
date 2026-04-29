# GET_RET_FLAG_SUBS

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This function retrieves the most recent 'TREATMENT_KEY' associated with a given subscription ID and campaign date, specifically for 'RET' action categories. It considers entries where the campaign date falls within the offer's start and end dates. It returns -2 for invalid input parameters or if no matching treatment key is found.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
| Column Name |
|---|
| TREATMENT_KEY |
| START_DATE |
| SUBSCRIPTION_ID |
| ACTION_CATEGORY |
| END_DATE |


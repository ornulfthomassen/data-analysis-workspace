# GET_RET_FLAG_KURT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Retrieves the highest priority 'RET' treatment key for a given Kurt ID and campaign date. It filters records from `ADM_QUAL_OFFER_HIST_SUBSCR` where the action category is 'RET' and the campaign date falls within the offer's start and end dates. Among the matching records, it selects the `TREATMENT_KEY` corresponding to the highest `CAMP_OFFER_PRIORITY` and, for ties, the most recent `START_DATE`. If no matching key is found, it returns -2.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
| Column Name |
|---|
| TREATMENT_KEY |
| CAMP_OFFER_PRIORITY |
| START_DATE |
| OWNER_KURT_ID |
| ACTION_CATEGORY |
| END_DATE |


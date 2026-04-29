# KIM_MAX_CONTACT_KEY_V

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the maximum 'CONTACT_KEY' from the 'KIM_CAMPAIGN_DETAIL_FACT' table, ensuring a default value of 0 if the table is empty or no contact keys are found.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
- ← [[DUAL]]


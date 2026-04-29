# KIM_FLAG_TREATMENT_KEY_UPDATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through records in the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table, specifically those where either the customer flag treatment key or subscription flag treatment key is -1 and the contact date is within the last 14 days (or a specified date). For these records, it calculates new flag treatment keys using external functions GET_RET_FLAG_KURT and GET_RET_FLAG_SUBS, and then updates the CUST_FLAG_TREATMENT_KEY and SUBS_FLAG_TREATMENT_KEY columns in the same table. It commits changes periodically for every 100,000 updated records.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| KURT_ID_OWNER |
| CONTACT_DTTM |
| CUST_FLAG_TREATMENT_KEY |
| SUBS_FLAG_TREATMENT_KEY |
| SUBSCRIPTION_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CUST_FLAG_TREATMENT_KEY |
| SUBS_FLAG_TREATMENT_KEY |


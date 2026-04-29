# V_A162_SAFE_ONB

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the latest campaign activity of type 'A162' (likely related to onboarding or a specific business process) for each unique customer. It retrieves customer identifier, program, activity ID, campaign, activity description, dialogue ID, and interaction code, considering data from March 2020 onwards.

## Data Sources (Inputs)
- ← [[crm_analyse.kim_campaign_detail_fact]]
| Column Name |
|---|
| contact_key |
| contact_dttm |
| kurt_id_owner |
| contact_month_key |
- ← [[crm_analyse.kim_campaign_detail_fact_ext]]
| Column Name |
|---|
| contact_key |
| program |
| activity_id |
| campaign |
| activity_desc |
| dialogue_id |
| interaction_cd |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |


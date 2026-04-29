# V_A164_SAFE_ONB

**Schema:** `CCM` | **Type:** `View`

## Description
Provides the most recent campaign activity details (specifically for activity_id 'A164') for each customer, incorporating customer and campaign information from various fact and mapping tables. It filters for contacts made since January 2020 and selects the latest activity per customer.

## Data Sources (Inputs)
- ← [[crm_analyse.kim_campaign_detail_fact]]
| Column Name |
|---|
| contact_key |
| kurt_id_owner |
| contact_month_key |
| contact_dttm |
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
| customer_sk |
| kurt_id |


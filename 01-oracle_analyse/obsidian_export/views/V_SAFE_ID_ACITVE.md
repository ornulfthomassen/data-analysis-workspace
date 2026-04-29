# V_SAFE_ID_ACITVE

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the activation status (active/inactive) and the earliest activation date for specific ID monitoring features (email verification, credit card monitoring, VPN token creation) for each unique customer. It aggregates action descriptions to determine if a feature has been activated and when it was first activated.

## Data Sources (Inputs)
- ← [[CLM_CCM.v_ccm_agrm_sfty_use]]
| Column Name |
|---|
| action_description |
| first_date |
| kurt_id |
- ← [[CLM_ADM.adm_customer_mapping]]
| Column Name |
|---|
| customer_sk |
| kurt_id |


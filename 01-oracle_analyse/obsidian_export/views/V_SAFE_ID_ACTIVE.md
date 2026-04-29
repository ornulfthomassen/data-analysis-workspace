# V_SAFE_ID_ACTIVE

**Schema:** `CCM` | **Type:** `View`

## Description
Summarizes the activation status of various Safe ID features (email verification, credit card monitoring, VPN token creation) for customers. It groups these activities by customer, customer life-phase segment, and the truncated first date of activity, providing flags (1 for active, 0 for inactive) for each specific action type.

## Data Sources (Inputs)
- ← [[CLM_CCM.v_ccm_agrm_sfty_use]]
| Column Name |
|---|
| kurt_id |
| first_date |
| action_description |
- ← [[CLM_ADM.adm_customer_mapping]]
| Column Name |
|---|
| customer_sk |
| kurt_id |
- ← [[CLM_CCM.ccm_customer_info_2]]
| Column Name |
|---|
| clm_livsfase_segment_name |
| kurt_id |


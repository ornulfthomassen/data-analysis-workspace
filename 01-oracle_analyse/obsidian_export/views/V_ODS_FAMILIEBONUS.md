# V_ODS_FAMILIEBONUS

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and details information about 'FamilieBonus' agreements, rewards, and associated customer roles. It combines agreement details, reward statistics, member-specific dates, subscription information, and customer mapping identifiers, specifically filtering for agreements related to a particular product ID (951) and calculating active flags based on agreement and member end dates.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
| Column Name |
|---|
| agreement_id |
| agreement_start_date |
| agreement_end_date |
| agreement_type |
| agreement_status |
| agreement_days_active |
| kurt_id |
| src_agreement_product_id |
- ← [[clm_ccm.v_ods_agrmt_mob_reward_agg]]
| Column Name |
|---|
| agreement_id |
| reward_no_units_basis |
| reward_no_units_can_use |
| reward_allocateed_gb_sum |
- ← [[clm_ccm.v_ods_agrmt_mob_reward_det]]
| Column Name |
|---|
| agreement_id |
| kurt_member_start_date |
| kurt_member_end_date |
| kurt_id_member |
- ← [[ods.bmgm_accesses_kurt_ods]]
| Column Name |
|---|
| kurt_id |
| customer_role_id |
| unit_ccdw_key |
| unit_source_type |
| unit_product_key |
| unit_product_name |
| unit_reward_basis |
| unit_reward_can_use |
| kurt_id_user |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |


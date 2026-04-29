# V_ODS_AGRM_REWARD

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and transforms agreement, customer, and reward data specifically for 'Familiebonus-medlem' agreements. It joins several agreement-related detail and aggregate views with customer mapping information, calculates membership status and activity flags, and provides various agreement and reward metrics.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_mob]]
| Column Name |
|---|
| agreement_id |
| src_agrm_agreement_offer_id |
| agreement_type |
| agreement_status |
| agreement_start_date |
| agreement_end_date |
| kurt_id |
| agreement_product_name |
- ← [[clm_ccm.v_ods_agrmt_mob_reward_det]]
| Column Name |
|---|
| agreement_id |
| src_agrm_agreement_offer_id |
| kurt_member_end_date |
| unit_product_name |
| kurt_member_start_date |
| unit_reward_can_use |
| kurt_id_member |
| unit_type |
| unit_ccdw_key |
| unit_reward_basis |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |
- ← [[clm_ccm.v_ods_agrmt_mob_reward_agg]]
| Column Name |
|---|
| agreement_id |
| reward_no_units_basis |
| reward_no_units_can_use |
| reward_allocateed_gb_sum |


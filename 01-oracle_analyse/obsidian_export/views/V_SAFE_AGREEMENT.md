# V_SAFE_AGREEMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches agreement-related data, specifically focusing on mobile safety agreement offers. It integrates information from various sources including customer mapping, dealer dimensions, and additional customer details. The view standardizes product start and end dates by truncating them and derives an active product flag based on the product's end date.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]
| Column Name |
|---|
| agreement_id |
| src_agreement_id |
| src_agrm_agreement_offer_id |
| agreement_product_name |
| product_status |
| product_start_date |
| product_end_date |
| product_key |
| product_name |
| kurt_id |
- ← [[onl_rep.agreement_order_offer]]
| Column Name |
|---|
| agreement_offer_id |
| action_type_id |
| agreement_order_id |
- ← [[onl_rep.agreement_order]]
| Column Name |
|---|
| agreement_order_id |
| dealer_id |
- ← [[CLM_ADM.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |
- ← [[GALAXY.dealer_dim]]
| Column Name |
|---|
| source_dealer_id |
| end_dt_key |
| dealer_key |
- ← [[CLM_CCM.ccm_customer_info_2]]
| Column Name |
|---|
| kurt_id |
| clm_livsfase_segment_name |


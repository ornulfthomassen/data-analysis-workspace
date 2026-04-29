# SAFESEC_ID_THEFT_WEEKLY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a weekly load of ID theft insurance data for the 'viya' system. This insurance is sold by dealers and is not part of the 'SAFE' system, focusing on specific product IDs (53029 and 771) and valid agreement dates.

## Data Sources (Inputs)
- ← [[ods.agreement_ods_mob]]
| Column Name |
|---|
| agreement_id |
| src_agrm_agreement_offer_id |
| root_product_offer_id |
| src_product_id |
| product_offer_id |
| start_date |
| end_date |
| customer_id_owner |
| SRC_PRODUCT_ID |
| SRC_ROOT_PRODUCT_ID |
- ← [[galaxy.product_dim]]
| Column Name |
|---|
| product_key |
| product_desc |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |
- ← [[galaxy.date_dim_mv]]
| Column Name |
|---|
| day |
| year_week_number |
| last_week |
- ← [[onl_rep.agreement_order_offer]]
| Column Name |
|---|
| agreement_offer_id |
| product_offer_id |
| action_type_id |
| agreement_order_id |
- ← [[ONL_REP.agreement_order]]
| Column Name |
|---|
| agreement_order_id |
| dealer_id |
- ← [[galaxy.dealer_dim]]
| Column Name |
|---|
| source_dealer_id |
| current_status |
| dealer_key |
| drm_sales_channel_gen02_desc |
| drm_sales_channel_gen03_desc |
| drm_sales_channel_gen04_desc |
| drm_sales_channel_gen07_desc |


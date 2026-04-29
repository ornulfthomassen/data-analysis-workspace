# V_IMEI_LIVE_EURKA

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated and filtered list of the most recent active product and customer details for each unique IMEI. It combines information from IMEI usage, subscription details, primary product dimensions, and customer mappings. The filtering ensures only specific subscription types, market areas, and product categories are included, and it prioritizes records with the latest terminal usage dates.

## Data Sources (Inputs)
- ← [[live.eureka_imei]]
| Column Name |
|---|
| imei |
| terminal_use_first_date |
| terminal_use_last_date |
| directory_number_id |
- ← [[galaxy.subscr_detail_fact]]
| Column Name |
|---|
| main_number |
| subscr_type_status_key |
| market_area_key |
| prim_prod_end_dt_key |
| prim_product_key |
| user_customer_key |
| prim_prod_start_dt_key |
- ← [[galaxy.primary_product_dim_v]]
| Column Name |
|---|
| prim_product_key |
| primary_product_flag |
| drm_common_product_group |
| drm_common_product_category |
| drm_common_product_area |
| prim_product_desc |
- ← [[clm_adm.adm_customer_mapping]]
| Column Name |
|---|
| kurt_id |
| customer_sk |


# PI_SUB_HIST_UP

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts filtered mobile telephony subscription details and history from subscription, subscription detail, and primary product dimension tables. It selects specific attributes like subscription key, source product ID, and product start/end dates, applying various filters on product categories, market areas, and subscription characteristics.

## Data Sources (Inputs)
- ← [[galaxy.subscription_dim_mv]]
| Column Name |
|---|
| subscription_key |
- ← [[galaxy.subscr_detail_fact]]
| Column Name |
|---|
| prim_prod_start_dt_key |
| prim_prod_end_dt_key |
| subscription_key |
| prim_product_key |
| subscr_quantity |
| market_area_key |
- ← [[galaxy.primary_product_dim_v]]
| Column Name |
|---|
| source_product_id_1 |
| prim_product_key |
| drm_common_product_category |
| drm_common_product_group |
| drm_common_product_area |
| source_system_name |
| prim_product_paytype |
| primary_product_flag |


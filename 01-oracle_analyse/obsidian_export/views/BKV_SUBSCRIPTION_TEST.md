# BKV_SUBSCRIPTION_TEST

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of active mobile subscription details, including associated product information and commercial customer data, linking subscriptions to their primary numbers and handling specific customer segment logic.

## Data Sources (Inputs)
- ← [[galaxy.subscription_dim]]
| Column Name |
|---|
| main_number |
| market_area_desc |
| subscription_key |
| parent_subscription_key |
| imei_last_used |
| imsi_number |
- ← [[galaxy.subscr_detail_fact]]
| Column Name |
|---|
| sub_number |
| subscription_key |
| prim_product_key |
| source_system_key |
| prim_prod_end_Dt_key |
| owner_customer_key |
- ← [[galaxy.product_dim]]
| Column Name |
|---|
| product_brand |
| drm_common_market_product |
| drm_market_product_group |
| drm_common_payment |
| product_key |
- ← [[galaxy.customer_dim]]
| Column Name |
|---|
| COMMERSIAL_CUSTOMER_NAME |
| current_company_family |
| COM_CUSTOMER_SEGMENT |
| COM_CUSTOMER_EMPLOYEES |
| CUSTOMER_KEY |


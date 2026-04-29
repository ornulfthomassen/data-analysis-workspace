# SUBS_PROD

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a combined view of subscribed products, enriching subscription details with product names from a product dimension table.

## Data Sources (Inputs)
- ← [[ccdw.subscribed_product]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| RESOURCE_VALUE |
| SUBSCRIPTION_SEQ |
| PRODUCT_CATEGORY_ID |
| SOURCE_SYSTEM_ID |
| BUSINESS_AREA_ID |
| START_DATE |
| END_DATE |
| INFO_CHG_DATE |
| RUN_ID |
| SEQ_ID |
| BINDING_START_DATE |
| BINDING_END_DATE |
| TERMINATION_FIXED_FEE |
| TERMINATION_MONTH_FEE |
| SYSTEM_COMPONENT_ID |
| COMOYO_USER_ID |
- ← [[galaxy.product_dim]]
| Column Name |
|---|
| product_name |
| product_key |


# MBB_SP

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves details of subscribed products, enriching them with the product name and description by joining with a product type configuration table. It specifically filters for products belonging to a predefined set of parent product categories.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
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
| BSB_AGREEMENT_ID |
| BSB_AGREE_PRODUCT_OFFER_ID |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| PRODUCT_NAME |
| DESCRIPTION |
| ID |
| PARENT |



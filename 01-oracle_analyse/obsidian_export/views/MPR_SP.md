# MPR_SP

**Schema:** `CCM` | **Type:** `View`

## Description
This view enriches subscribed product data by joining it with product type configuration information. It retrieves product names and descriptions from the `CCM_PRODUCT_TYPE_CONFIG` table, using a self-join on parent-child relationships, and filters for specific product categories.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SUBSCRIPTION_ID |
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
| ID |
| PARENT |
| PRODUCT_NAME |
| DESCRIPTION |


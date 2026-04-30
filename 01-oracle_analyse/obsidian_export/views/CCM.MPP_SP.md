# MPP_SP

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive look at subscribed products, enriching them with product names and descriptions obtained from the product type configuration tables, specifically filtering for products belonging to certain parent categories.

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
| ID |
| PARENT |
| DESCRIPTION |



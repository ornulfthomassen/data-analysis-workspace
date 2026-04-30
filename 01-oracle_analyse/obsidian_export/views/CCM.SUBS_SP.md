# SUBS_SP

**Schema:** `CCM` | **Type:** `View`

## Description
Enriches subscribed product information by joining subscription details with product dimensions and product type configurations.

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

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PRODUCT_NAME |
| PARENT |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| DESCRIPTION |



# MBB_S

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "MBB_S", consolidates detailed subscription records from the CCDW.SUBSCRIPTION table. It enriches the subscription data by joining with product dimension data from GALAXY.PRODUCT_DIM and retrieves product names and descriptions from CLM_CCM.CCM_PRODUCT_TYPE_CONFIG, specifically filtering for product types with parent IDs 3, 25, 35, or 63. The primary goal is to provide a comprehensive view of subscriptions with associated product configuration details.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| PRODUCT_NAME |
| SUBSCRIPTION_ID |
| PRODUCT_CATEGORY_ID |
| PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
| KURT_ID_OWNER |
| KURT_ID_PAYER |
| KURT_ID_USER |
| KURT_ID_USER_2 |
| SOURCE_SYSTEM_ID |
| BUSINESS_AREA_ID |
| DEALER_ID |
| ACCOUNT_ID |
| MAIN_NUMBER |
| USER_ID |
| ORIGINAL_START_DATE |
| START_DATE |
| END_DATE |
| INFO_CHG_DATE |
| PARENT_SUBSCRIPTION_ID |
| BINDING_START_DATE |
| BINDING_END_DATE |
| CURRENT_STATUS |
| SECRET_NUMBER_FLAG |
| TERMINATION_REASON |
| SOURCE_OWNER_ID |
| SOURCE_PAYER_ID |
| SOURCE_USER_ID |
| RUN_ID |
| SEQ_ID |
| PRIORITY_FLAG |
| OPERATIONAL_STABILITY_DESC |
| SOURCE_VALID_FROM_DATE |
| SOURCE_VALID_TO_DATE |
| PRIM_PROD_VALID_FROM_DATE |
| PRIM_PROD_VALID_TO_DATE |
| BSB_AGREEMENT_ID |
| BSB_AGREE_OWNER_KURT_ID |
| BSB_AGREE_PAYER_KURT_ID |
| BSB_AGREE_ACCOUNT_ID |
| BSB_AGREE_ACC_OWNER_KURT_ID |
| BSB_AGREE_PRODUCT_OFFER_ID |
| CUST_UNIT_NUMBER_OWNER |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| PRODUCT_NAME |
| DESCRIPTION |


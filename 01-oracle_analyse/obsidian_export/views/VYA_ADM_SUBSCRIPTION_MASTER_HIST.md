# VYA_ADM_SUBSCRIPTION_MASTER_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates historical subscription master data, enriching it with main subscription numbers and customer surrogate keys for the owner, payer, and last user. It tracks various subscription attributes and their previous values over time, providing a comprehensive historical view of subscriptions.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| MAIN_NUMBER_SK |
| MAIN_NUMBER_RANK |
| SUBSCR_ID_NUM |
| SUBSCRIPTION_ID |
| FIRST_PARENT_SUBSCRIPTION_ID |
| LAST_PARENT_SUBSCRIPTION_ID |
| SUBSCR_TYPE |
| SUBSCRIPTION_ID_PREV |
| DAYS_BETWEEN_SUBSCRIPTIONS |
| MARKET_AREA_ID |
| MARKET_AREA_ID_PREV |
| SUBSCR_START_REASON |
| MARKET_AREA_START |
| OWNER |
| PAYER |
| LAST_USER |
| NEW_USER_IND |
| ORIGINAL_START_DATE |
| ORIGINAL_START_DATE_PREV |
| END_DATE |
| END_DATE_PREV |
| CURRENT_STATUS |
| PRODUCT_GROUP |
| FIRST_PRODUCT_KEY |
| LAST_PRODUCT_KEY |
| NO_PRODUCT_COUNT |
| FIRST_PRODUCT_KEY_PREV |
| LAST_PRODUCT_KEY_PREV |
| NO_PRODUCT_COUNT_PREV |
| PORT_IN_DATE |
| PORT_IN_DEALER_ID |
| PORT_IN_SERV_PROV_ID |
| PORT_OUT_DATE |
| PORT_OUT_DEALER_ID |
| PORT_OUT_SERV_PROV_ID |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |


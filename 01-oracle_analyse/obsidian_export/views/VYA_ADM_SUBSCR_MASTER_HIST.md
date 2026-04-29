# VYA_ADM_SUBSCR_MASTER_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ADM_SUBSCR_MASTER_HIST, provides a comprehensive historical record of subscriptions, enriching subscription details from ADM_SUBSCRIPTION_MASTER_HIST with customer ownership and user information from ADM_CUSTOMER_MAPPING. It processes and consolidates various subscription attributes, including parent subscriptions, market area details, start/end dates, current status, product group information, and porting details, for both owners and users, primarily focusing on data from the last two years.

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
| SUBSCRIPTION_ID_ORIG |
| SUBSCRIPTION_ID_PAST |
| DAYS_BETWEEN_SUBSCRIPTIONS |
| SUBSCRIPTION_ID_PAST_ORIG |
| MARKET_AREA_ID |
| MARKET_AREA_ID_PREV |
| PORT_IN_DATE |
| SUBSCR_START_REASON |
| MARKET_AREA_START |
| NEW_USER_IND |
| ORIGINAL_START_DATE |
| END_DATE |
| END_DATE_PREV |
| CURRENT_STATUS |
| PRODUCT_GROUP |
| FIRST_PRODUCT_KEY |
| LAST_PRODUCT_KEY |
| NO_PRODUCT_COUNT |
| LAST_PRODUCT_KEY_PREV |
| PORT_IN_DEALER_ID |
| PORT_IN_SERV_PROV_ID |
| PORT_OUT_DATE |
| PORT_OUT_DEALER_ID |
| PORT_OUT_SERV_PROV_ID |
| OWNER |
| LAST_USER |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |


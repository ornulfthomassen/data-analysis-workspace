# GCP_SUBSCRIPTION_MASTER_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive historical record of subscription data, enriching it with derived flags like 'USER_BECAME_OWNER_FLAG' based on changes in ownership, previous subscription details, market areas, and product information. It consolidates various attributes related to the lifecycle and changes of subscriptions.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| MAIN_NUMBER_RANK |
| SUBSCR_ID_NUM |
| FIRST_PARENT_SUBSCRIPTION_ID |
| LAST_PARENT_SUBSCRIPTION_ID |
| SUBSCR_TYPE |
| SUBSCRIPTION_ID_PREV |
| DAYS_BETWEEN_SUBSCRIPTIONS |
| MARKET_AREA_ID |
| MARKET_AREA_ID_PREV |
| MARKET_AREA_ID_ORIG |
| SUBSCR_START_REASON |
| OWNER |
| LAST_USER_PREV |
| OWNER_PREV |
| MARKET_AREA_START |
| NEW_USER_IND |
| ORIGINAL_START_DATE |
| ORIGINAL_START_DATE_PREV |
| ORIGINAL_START_DATE_ORIG |
| END_DATE |
| END_DATE_PREV |
| END_DATE_ORIG |
| CURRENT_STATUS |
| PRODUCT_GROUP |
| FIRST_PRODUCT_KEY |
| LAST_PRODUCT_KEY |
| NO_PRODUCT_COUNT |
| FIRST_PRODUCT_KEY_PREV |
| LAST_PRODUCT_KEY_PREV |
| NO_PRODUCT_COUNT_PREV |
| FIRST_PRODUCT_KEY_ORIG |
| LAST_PRODUCT_KEY_ORIG |
| NO_PRODUCT_COUNT_ORIG |
| PORT_IN_DATE |
| PORT_IN_DEALER_ID |
| PORT_IN_SERV_PROV_ID |
| PORT_OUT_DATE |
| PORT_OUT_DEALER_ID |
| PORT_OUT_SERV_PROV_ID |


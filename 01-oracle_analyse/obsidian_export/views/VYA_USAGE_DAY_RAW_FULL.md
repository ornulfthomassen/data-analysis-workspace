# VYA_USAGE_DAY_RAW_FULL

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates daily mobile subscription usage data, enriching it with monthly dimension details, subscription core information, and customer owner/user mappings. It includes specific logic to handle twin subscriptions and to anonymize sensitive data like subscriber numbers (SUB_NUMBER) and IMEI by replacing or hashing them, focusing on recent usage periods.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MONTH_NAME |
| FIRST_DATE_KEY |
| LAST_DATE_KEY |
| RELATIVE_MONTH |
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]
| Column Name |
|---|
| EVENT_DATE_KEY |
| LOAD_DATE_KEY |
| PARENT_SUBSCRIPTION_KEY |
| SUBSCRIPTION_KEY |
| SUB_NUMBER |
| PRIM_PRODUCT_KEY |
| DISCOUNT_PRODUCT_OFFER_KEY |
| SUBSCRIPTION_TYPE_STATUS_KEY |
| ACCOUNT_KEY |
| MARKET_AREA_KEY |
| DESTINATION_COUNTRY_KEY |
| ROAMING_COUNTRY_KEY |
| CALL_TYPE_KEY |
| NETWORK_OPERATOR_KEY |
| TRAFFIC_TYPE_KEY |
| AGREEMENT_KEY |
| AGREEMENT_OFFER_KEY |
| TWIN_SWITCH_KEY |
| IMEI |
| IMSI |
| HANDSET_KEY |
| APN_KEY |
| PRICE_CATEGORY_KEY |
| DISCOUNT_TYPE_KEY |
| DISCOUNT_RATE |
| REVENUE_CATEGORY_KEY |
| CPA_BUSINESS_MODEL_KEY |
| CONTENT_PROVIDER_KEY |
| CALL_START_PRICE |
| USAGE_NET_DISCOUNT_AMOUNT |
| USAGE_GROSS_DISCOUNT_AMOUNT |
| USAGE_NET_AMOUNT |
| USAGE_GROSS_AMOUNT |
| USAGE_VOLUME_DOWN |
| USAGE_VOLUME_TOTAL |
| USAGE_DURATION |
| TOTAL_ROAMING_COST |
| COST_OF_VALUE |
| USAGE_NUMBER_OF_EVENTS |
| USAGE_NUMBER_OF_CDR |
| SUBSCR_OWNER_KEY |
| SUBSCR_USER_KEY |
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |


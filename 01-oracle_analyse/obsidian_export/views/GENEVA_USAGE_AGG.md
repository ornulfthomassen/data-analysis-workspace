# GENEVA_USAGE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly subscription usage data from the GALAXY schema, joining it with product, CPA business model, and traffic type dimensions from GALAXY and CRM_ANALYSE schemas. It calculates various usage metrics such as net/gross amounts, discounts, call start prices, and differentiated volumes/events/durations based on traffic type, grouped by various keys and descriptive attributes.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_USAGE_MONTH_FACT_V]]
| Column Name |
|---|
| PERIOD_ID_EVENT_DATE |
| SUBSCRIPTION_KEY |
| MARKET_AREA_KEY |
| AGREEMENT_OFFER_KEY |
| AGREEMENT_KEY |
| DISCOUNT_TYPE_KEY |
| CALL_TYPE_KEY |
| HANDSET_KEY |
| ROAMING_COUNTRY_KEY |
| DESTINATION_COUNTRY_KEY |
| TWIN_SWITCH_KEY |
| APN_KEY |
| CONTENT_PROVIDER_KEY |
| DISCOUNT_RATE |
| DISCOUNT_PRODUCT_OFFER_KEY |
| CPA_BUSINESS_MODEL_KEY |
| PRIM_PRODUCT_KEY |
| TRAFFIC_TYPE_KEY |
| SUB_NUMBER |
| TRAFFIC_NET_AMOUNT |
| TRAFFIC_GROSS_AMOUNT |
| TRAFFIC_NET_DISCOUNT_AMOUNT |
| TRAFFIC_GROSS_DISCOUNT_AMOUNT |
| TRAFFIC_CALL_START_PRICE |
| TRAFFIC_VOLUME_TOTAL |
| TRAFFIC_NUMBER_EVENTS |
| TRAFFIC_DURATION |
| SOURCE_SYSTEM_KEY |
- ← [[GALAXY.CPA_BUSINESS_MODEL_DIM_V]]
| Column Name |
|---|
| CPA_BUSINESS_MODEL_ID |
| CPA_BUSINESS_MODEL_NAME |
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_POID |
| PRODUCT_REPORT_LEVEL1 |
| PRODUCT_REPORT_LEVEL2 |
| PRODUCT_REPORT_LEVEL3 |
| PRODUCT_REPORT_LEVEL4 |
| PRODUCT_PORTFOLIO |
- ← [[GALAXY.TRAFFIC_TYPE_DIM_V]]
| Column Name |
|---|
| TRAFFIC_TYPE_KEY |
| REPORT_GROUP_1 |
| REPORT_GROUP_2 |
| REPORT_GROUP_3 |
| REPORT_GROUP_4 |
| TRAFFIC_TYPE_NAME_1 |
| TRAFFIC_TYPE_NAME_2 |
| TRAFFIC_TYPE_NAME_3 |
| TRAFFIC_TYPE_NAME_4 |


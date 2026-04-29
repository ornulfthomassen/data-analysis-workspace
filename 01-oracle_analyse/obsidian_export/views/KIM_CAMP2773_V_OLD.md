# KIM_CAMP2773_V_OLD

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates detailed campaign interaction data from 'kim_campaign_detail_fact' for a specific campaign ('CAMP2773'). It enriches this data with communication details from 'kim_communication_dim' and links it to relevant online service order product information from 'V_ONL_SERVICE_ORDER_PRODUCT'. The linkage to service orders is based on the main phone number and a temporal window, specifically matching 'PE' (Product Event) actions that occurred between order arrival and processed dates, and before the campaign contact datetime. The view also filters for contacts made on or after January 1, 2017, and with valid main numbers, providing a comprehensive dataset for analyzing this particular campaign's performance and customer interactions.

## Data Sources (Inputs)
- ← [[crm_analyse.kim_campaign_detail_fact]]
| Column Name |
|---|
| VOLUME |
| USER_HOUSEHOLD_ID |
| TREATMENT_PRODUCT_KEY |
| TREATMENT_PRIORITY |
| TREATMENT_KEY |
| TREATMENT_HASH_VAL |
| SUBSCRIPTION_SEGMENT_KEY |
| SUBSCRIPTION_KEY |
| SUBS_TRAFFIC_GROUP_KEY |
| SUBS_FLAG_TREATMENT_KEY |
| SUBS_DATA_GROUP_KEY |
| SOURCE_SYSTEM_KEY |
| SOURCE_CONTACT_ID |
| SEQ_ID_UPD |
| SEQ_ID |
| SALES_MATRIX |
| RUN_ID |
| RESPONSE_REASON_KEY |
| RESPONSE_KEY |
| RESPONSE_DATE_KEY |
| RESPONSE_CHANNEL_KEY |
| PROFIT_ID |
| PRESENTED_KEY |
| PRESENTED_DURATION_KEY |
| PRESENTED_DATE_KEY |
| ORDER_TO_PRODUCT_KEY |
| ORDER_STATUS_KEY |
| ORDER_STATUS_DT_KEY |
| ORDER_SOURCE_SYSTEM_KEY |
| ORDER_SERVICE_PROVIDER_KEY |
| ORDER_RANK_GROUP_KEY |
| ORDER_RANK |
| ORDER_MATCH_KEY |
| ORDER_LINE_TYPE_KEY |
| ORDER_ID |
| ORDER_HANDSET_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_DT_KEY |
| ORDER_DEALER_KEY |
| ORDER_DAYS |
| ORDER_CAPTURE_DAYS |
| ORDER_BINDING_PRODUCT_KEY |
| MEASURE_TYPE |
| MAIN_NUMBER |
| KURT_ID_USER |
| KURT_ID_PAYER |
| KURT_ID_OWNER |
| KPI_PRODUCT_CHANGE |
| KPI_NEWSALE |
| IS_SUBS_CAMP |
| GENDER |
| CUST_STRATEGIC_SEGMENT_KEY |
| CUST_SEGMENT_KEY |
| CUST_RESPONSE_KEY |
| CUST_HOUSEHOLD_ID |
| CUST_FLAG_TREATMENT_KEY |
| CUST_FAR_ID |
| CUST_AGE_GROUP_KEY |
| CUST_AGE |
| CONTACTED_BIND_START_DATE_KEY |
| CONTACTED_BIND_END_DATE_KEY |
| CONTACT_TIME_KEY |
| CONTACT_TEAM |
| CONTACT_SECONDS |
| CONTACT_PRODUCT_KEY |
| CONTACT_MONTH_KEY |
| CONTACT_LOCATION |
| CONTACT_KEY |
| CONTACT_HANDSET_KEY |
| CONTACT_DTTM |
| CONTACT_DELAY_DAYS |
| CONTACT_DATE_KEY |
| CONN_ID |
| COMMUNICATION_KEY |
| CHURN_GROUP_KEY |
| CHANNEL_KEY |
| CELL_PACKAGE_SK |
| CAMPAIGN_TYPE_DESC |
| CAMPAIGN_KEY |
| CAMPAIGN_HIT_TYPE_KEY |
| BINDING_BENEFIT_DESC |
- ← [[crm_analyse.kim_campaign_dim]]
| Column Name |
|---|
| CAMPAIGN_KEY |
| CAMPAIGN_CD |
- ← [[crm_analyse.kim_communication_dim]]
| Column Name |
|---|
| COMMUNICATION_KEY |
| COMMUNICATION_CD |
| COMMUNICATION_NM |
| COMMUNICATION_DESC |
| ACTION_CATEGORY |
| OFFER_CATEGORY |
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| AUTO_ORDER_QUEUE_ID |
| COMMISSION_STATUS_ID |
| CUST_TYPE_ID |
| DEALER_ID |
| EQ_UNIQUE_NUM |
| ORDER_ARRIVAL_DATE |
| ORDER_ID |
| ORDER_LINE_ID |
| ORDER_PHONE_NUM |
| ORDER_PROCESSED_DATE |
| ORDER_QUEUE_ID |
| PARAM_COUNT |
| PARENT_ORDER_LINE_ID |
| PRICE_PLAN_TYPE_ID |
| PRODUCT_ACTION_TYPE_ID |
| PRODUCT_CODE_ID |
| PRODUCT_ID |
| PRODUCT_PRIORITY |
| PRODUCT_PROCESSED_DATE |
| PRODUCT_RESPONSE_TIME |
| PRODUCT_STATUS_AUTOREG |
| PRODUCT_STATUS_BACK_END |
| PRODUCT_STATUS_ID |
| PRODUCT_STATUS_REASON_ID |
| SUBSCR_ID |
| USER_ID |


# CHURN_FORECAST_ST_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'CHURN_FORECAST_ST_V', serves as a staging table for churn forecasting within the CRM_ANALYSE schema. It integrates data from mobile porting reports, detailed subscription history, product configuration, and profit segments. The view consolidates information on customer porting activities, associated order details, extensive mobile subscription attributes (including historical changes), and product classifications, enriching the data with profit category information. It filters for specific market areas, recent porting events (last 24 months), and particular order statuses, providing a comprehensive dataset for analyzing and predicting customer churn.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
| Column Name |
|---|
| PORT_DATE |
| FETCHED_DATE |
| INFO_CHG_DATE |
| ORDER_ARRIVAL_DATE |
| ORDER_ID |
| ORDER_PHONE_NUM |
| ORDER_STATUS_ID |
| SERVICE_PROVIDER_ID_OUT |
| SERVICE_PROVIDER_ID_OUT_NAME |
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
| Column Name |
|---|
| ACC_ID |
| CUST_FIRST_NAME |
| CUST_ID_PAYER |
| CUST_ID_RESP |
| CUST_ID_USER |
| CUST_LAST_NAME |
| CUST_MIDDLE_NAME |
| CUST_UNIT_DATE |
| CUST_UNIT_NUMBER |
| DIRECTORY_NUMBER_ID |
| KURT_ID |
| PRODUCT_ID |
| S212_PRODUCT_ID |
| STATUS |
| SUBSCR_ID |
| SUBSCR_VALID_FROM_DATE |
| UNIT_TYPE_ID |
| ORDER_ID |
| ORDER_ARRIVAL_DATE |
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
| SUBSCRIPTION_KEY_PREV |
| SUBSCRIPTION_KEY_ORIG |
| MARKET_AREA_ID |
| MARKET_AREA_ID_PREV |
| MARKET_AREA_ID_ORIG |
| SUBSCR_START_REASON |
| CHANGETYPE_START |
| OWNER |
| OWNER_PREV |
| OWNER_ORIG |
| FIRST_USER |
| LAST_USER |
| FIRST_USER_PREV |
| LAST_USER_PREV |
| FIRST_USER_ORIG |
| LAST_USER_ORIG |
| NEW_USER_IND |
| ORIGINAL_START_DATE |
| ORIGINAL_START_DATE_PREV |
| ORIGINAL_START_DATE_ORIG |
| START_DATE |
| START_DATE_PREV |
| START_DATE_ORIG |
| END_DATE |
| END_DATE_ORIG |
| CURRENT_STATUS |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_PAYMENT_PREV |
| DRM_COMMON_PAYMENT_ORIG |
| FIRST_PRODUCT_OFFER_ID |
| LAST_PRODUCT_OFFER_ID |
| FIRST_PRODUCT_OFFER_ID_PREV |
| LAST_PRODUCT_OFFER_ID_PREV |
| FIRST_PRODUCT_OFFER_ID_ORIG |
| LAST_PRODUCT_OFFER_ID_ORIG |
| DEALER_KEY |
| DEALER_KEY_PREV |
| DEALER_KEY_ORIG |
| DEALER_NAME |
| DEALER_NAME_PREV |
| DEALER_NAME_ORIG |
| DEALER_SALES_CHANNEL_TYPE |
| DEALER_SALES_CHANNEL_TYPE_PREV |
| DEALER_SALES_CHANNEL_TYPE_ORIG |
| DEALER_CHAIN |
| DEALER_CHAIN_PREV |
| DEALER_CHAIN_ORIG |
| PORT_IN_DATE |
| PORT_IN_DEALER_ID |
| PORT_IN_SERV_PROV_ID |
| PORT_IN_SERV_PROV_NAME |
| SUBSCRIPTION_ID |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PRODUCT_BRAND |
| PRODUCT_NAME |
| TYPE |
| PARENT |
| DESCRIPTION |
| VALUE |
- ← [[CRM_ANALYSE.PROFITSEGMENT_MOBILE]]
| Column Name |
|---|
| SEGMENT_ID |
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
- ← [[PROFIT.CP_CAT_BED_PRIV]]
| Column Name |
|---|
| CATEGORY |
| SUBSCR_ID |
| PERIOD_ID |


# VYA_ORDER_LINE_DETAIL_FACT_HW

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ORDER_LINE_DETAIL_FACT_HW, extracts and transforms hardware order line item details from various operational and analytical sources. Its main purpose is to load hardware order data, including customer, product, date, and sales-related information, into a fact table within the 'Mjøsa' data warehouse for 'telenor.no' online store analytics and KPI calculations.

## Data Sources (Inputs)
- ← [[ONL_REP.MOOA_ORDER_LINK]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| SERVICE_ORDER_ID |
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| SOURCE_APPLICATION_ID |
| DEALER_ID |
| ORDER_TYPE |
| STATUS_ID |
| CUSTOMER_ID |
| SALES_REP_NAME |
| INFO_REG_DATE |
| INFO_CHG_DATE |
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| PRODUCT_LINE_ID |
| ACTION_TYPE_ID |
| PRODUCT_OFFER_ID |
| STATUS_ID |
- ← [[FPS.TERMINAL_GTIN]]
| Column Name |
|---|
| IMEI |
| GTIN |
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| PRODUCT_LINE_ID |
| PARAMETER_ID |
| ACTION_TYPE_ID |
| STATUS_ID |
| PARAMETER_VALUE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_KEY |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| CURRENT_STATUS |
| DEALER_KEY |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| WEEK_NUMBER |
| RELATIVE_WEEK |
| MONTH_NUMBER |
| RELATIVE_MONTH |
| YEAR |
| YEAR_WEEK_NUMBER |
| YEAR_MONTH_NUMBER |
| YEAR_QUARTER_NUMBER |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| KURT_ID |
| CUST_UNIT_DATE |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_KEY |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_KEY |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| MAIN_NUMBER |
| CUSTOMER_ROLE_ID |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
| CUSTOMER_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| CUSTOMER_KEY |
| MAIN_ADDRESS_LOCATION_ID |
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
| Column Name |
|---|
| SUBSCR_USER_LOC_KEY |
| SUBSCR_USER_POSTCODE_ID |
| SUBSCR_USER_MUNICIPAL_ID |
| SUBSCR_USER_MUNICIPAL |
| SUBSCR_USER_COUNTY_ID |
| SUBSCR_USER_COUNTY |


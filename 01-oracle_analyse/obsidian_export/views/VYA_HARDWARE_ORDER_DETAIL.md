# VYA_HARDWARE_ORDER_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to consolidate and enrich hardware order data for analytical purposes, specifically for use in Viya, originating from the Telenor.no webshop. It integrates details about hardware orders, associated service orders, agreement information (like swap, insurance, and downpayment products), product specifications (GTIN properties, handset details), and customer demographics (age, location, subscription data) to provide a comprehensive dataset for sales and product analysis.

## Data Sources (Inputs)
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| DEALER_ID |
| ORDER_TYPE |
| STATUS_ID |
| CUSTOMER_ID |
| SALES_REP_NAME |
| INFO_REG_DATE |
| INFO_CHG_DATE |
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
| Column Name |
|---|
| GTIN |
| MANUFACTURER |
| MODEL_NAME |
| COLOR_NAME |
| TOTAL_SIZE |
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| HARDWARE_ORDER_ID |
| PRODUCT_LINE_ID |
| ACTION_TYPE_ID |
| STATUS_ID |
| PARAMETER_ID |
| PARAMETER_VALUE |
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_ACTION_TYPE_ID |
| ORDER_STATUS_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ARRIVAL_DATE |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| PRODUCT_ACTION_TYPE_ID |
| SUBSCR_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| ACTION_TYPE_ID |
| PRODUCT_OFFER_ID |
| STATUS_ID |
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| START_DATE |
| END_DATE |
| MONTHLY_FEE |
| PRODUCT_NAME |
| DRM_COMMON_MARKET_PRODUCT |
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| AGREEMENT_OFFER_ID |
| PRODUCT_OFFER_ID |
- ← [[CM.AGREEMENT_OFFER]]
| Column Name |
|---|
| AGREEMENT_OFFER_ID |
| VALID_TO_DATE |
| VALID_FROM_DATE |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| DRM_COMMON_TECHNOLOGY |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_MARKET_PRODUCT |
| PRODUCT_NAME_USE |
| PRODUCT_DESC |
| MONTHLY_PRICE |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_WEEK_NUMBER |
| RELATIVE_WEEK |
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
| Column Name |
|---|
| SOURCE_SYSTEM_STATUS_CODE |
| BUSINESS_AREA_NAME |
| ORDER_STATUS_NAME |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| CUST_UNIT_DATE |
| KURT_ID |
- ← [[GALAXY.CUSTOMER_DIM]]
| Column Name |
|---|
| CUSTOMER_KEY |
| MAIN_ADDRESS_LOCATION_ID |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_KEY |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_KEY |
| AGE_GROUP_NAME_10C |
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
| Column Name |
|---|
| MAIN_NUMBER |
| CUSTOMER_ROLE_ID |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| MARKET_AREA_ID |
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
| Column Name |
|---|
| SUBSCR_USER_LOC_KEY |
| SUBSCR_USER_POSTCODE_ID |
| SUBSCR_USER_MUNICIPAL_ID |
| SUBSCR_USER_MUNICIPAL |
| SUBSCR_USER_COUNTY_ID |
| SUBSCR_USER_COUNTY |
- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| MANUFACTURER |
| MARKETING_NAME |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |


# GCP_MOBILE_PORT_DATES_UPCOMING

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates information about upcoming mobile number porting orders (both 'inporting' and 'outporting') across various service providers (Telenor, Talkmore, Dipper, and external). It consolidates order details, customer roles, subscription information (where applicable), associated products, and calculates the porting date and days remaining until porting, based on service order and subscription management data.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ARRIVAL_DATE |
| ORDER_ID |
| ORDER_STATUS_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ACTION_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| ORDER_ID |
| CUST_ROLE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_PHONE_NUM |
| SUBSCR_ID |
| ORDER_ID |
| PRODUCT_ACTION_TYPE_ID |
| ORDER_LINE_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| ORIGINAL_START_DATE |
| PRODUCT_OFFER_ID |
| KURT_ID_OWNER |
| KURT_ID_USER |
| KURT_ID_PAYER |
| SUBSCRIPTION_ID |
| BUSINESS_AREA_ID |
| CURRENT_STATUS |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| PARAM_VALUE |
| ORDER_ID |
| ORDER_LINE_ID |
| PARAM_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |


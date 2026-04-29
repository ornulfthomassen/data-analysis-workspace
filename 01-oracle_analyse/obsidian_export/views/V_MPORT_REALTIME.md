# V_MPORT_REALTIME

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a unified, real-time view of mobile porting orders by consolidating data from service orders, products, subscriptions, and their associated parameters. It extracts key porting-related details such as service providers, IMEI numbers, and porting dates for recent customer orders, specifically those with a customer type 'P' and product offer category '10'.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_STATUS_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_PROCESSED_DATE |
| CUST_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| SUBSCR_ID |
| order_phone_num |
| PRODUCT_STATUS_ID |
| PRODUCT_ACTION_TYPE_ID |
| PRODUCT_NAME |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| PARAM_ID |
| PARAM_VALUE |
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_OFFER_CATEGORY_ID |
| ACTION_TYPE_ID |
| STATUS_ID |
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| PARAM_ID |
| PARAM_VALUE |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
| S212_PRODUCT_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| PRODUCT_BRAND |


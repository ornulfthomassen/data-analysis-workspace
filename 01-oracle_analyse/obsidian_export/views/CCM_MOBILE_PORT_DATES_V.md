# CCM_MOBILE_PORT_DATES_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a unified view of mobile number porting orders, combining both pending/in-progress orders with future port dates and recently completed orders. It retrieves details such as subscription ID, main phone number, port order identifiers, various dates related to porting, and order status, by joining service order information with product details and subscription mappings. The view filters orders by specific action types and status, and includes parameters related to the porting process.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_ARRIVAL_DATE |
| ORDER_STATUS_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ACTION_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_PHONE_NUM |
| SUBSCR_ID |
| PRODUCT_ACTION_TYPE_ID |
| ORDER_LINE_ID |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_LINE_ID |
| PARAM_ID |
| PARAM_VALUE |


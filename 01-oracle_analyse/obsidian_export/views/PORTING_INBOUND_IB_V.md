# PORTING_INBOUND_IB_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts recent 'new sale' service orders (customer type 'P') that are related to the 'GSM' product (PRODUCT_ID 11), have a 'Porting Inbound' product action type ('PI'), and are not in 'KB' or 'FB' product/order statuses. It enriches these selected orders with customer IDs for specific roles: Owner (CUST_ROLE_ID 6), Payer (CUST_ROLE_ID 7), and User (CUST_ROLE_ID 8).

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_STATUS_ID |
| ORDER_PROCESSED_DATE |
| ORDER_ARRIVAL_DATE |
| CUST_TYPE_ID |
| ORDER_ACTION_TYPE_ID |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_ID |
| PRODUCT_ACTION_TYPE_ID |
| PRODUCT_STATUS_ID |
| DEALER_ID |
| ORDER_PHONE_NUM |
| SUBSCR_ID |
| ORDER_LINE_ID |
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
- ← [[CLM_RTDM.V_ONL_SERVICE_ORDER_CUSTOMER]]
| Column Name |
|---|
| ORDER_ID |
| CUST_ID |
| CUST_ROLE_ID |


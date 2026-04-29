# V_SUBSCRIPTION_ORDER_STATUS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides core subscription identification details from the CCM_SUBSCRIPTION table, enriched with a derived order status. The order status is determined by analyzing recent service order product activities (specifically 'CH' for change and 'PE' for porting actions) and their statuses ('FB' for failed, 'IB' for in progress, 'KB' for completed) from the SERVICE_ORDER and SERVICE_ORDER_PRODUCT tables. It classifies these activities into user-friendly descriptions like 'CHANGE IN PROGRESS' or 'PORTING COMPLETED' based on the most recent status within a 6-hour window.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| USER_KURT_ID |
| OWNER_KURT_ID |
| PAYER_KURT_ID |
| SOURCE_SYSTEM_SUBSCR_ID_1 |
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_ARRIVAL_DATE |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_ACTION_TYPE_ID |
| PRODUCT_STATUS_ID |
| ORDER_PHONE_NUM |
| SUBSCR_ID |


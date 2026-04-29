# V_TALKMORE_PORTING

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the volume of distinct service orders related to 'porting in' (PI) or 'porting out' (PE) actions, specifically for service provider '705', for orders arriving from January 1, 2022, onwards. The data is aggregated by origin and destination service providers, order arrival date, product action type, order status, and customer type.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| Order_id |
| order_arrival_date |
| PRODUCT_ACTION_TYPE_ID |
| ORDER_STATUS_ID |
| cust_type_id |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| order_id |
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| order_id |
| Param_id |
| param_value |
- ← [[CCDW.SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER_ID |
| service_provider_name |


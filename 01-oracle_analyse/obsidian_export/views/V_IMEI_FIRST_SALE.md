# V_IMEI_FIRST_SALE

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies and retrieves the details (dealer key and sales date) of the latest completed sale for each unique IMEI. It filters sales data by specific business area (key = 2) and order status (key = 101), joining with a list of live IMEIs.

## Data Sources (Inputs)
- ← [[galaxy.order_line_detail_fact_mv]]
- ← [[ccm.v_imei_live_eurka]]


# V_IMEI_FIRST_SALE

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the primary or 'first sale' details for each unique IMEI, including the IMEI, associated dealer key, and the sales date, by selecting the most recent order status update record that meets specific order line and business area criteria.

## Data Sources (Inputs)
- ← [[galaxy.order_line_detail_fact_mv]]
| Column Name |
|---|
| imei |
| dealer_key |
| order_status_dt_key |
| order_status_time_key |
| order_key |
| orderline_product_key |
| order_line_status_key |
| business_area_key |
- ← [[ccm.v_imei_live_eurka]]
| Column Name |
|---|
| imei |


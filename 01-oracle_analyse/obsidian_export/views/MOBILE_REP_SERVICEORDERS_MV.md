# MOBILE_REP_SERVICEORDERS_MV

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `CCM.MOBILE_REP_SERVICEORDERS_MV`, is designed to provide a comprehensive analytical and reporting dataset for mobile service orders. It calculates various Key Performance Indicators (KPIs) such as new sales, product changes (upsale/downsale/neutral, with/without cross-brand), porting out, terminations, and swap activities. The view enriches core service order data with detailed product information (current and previous offers), device IMEI, porting details, associated dealer and sales channel attributes, and information about value-added services ('Goodies'). It filters orders processed within the last six months, focusing on specific order statuses and customer types, making it suitable for operational and strategic analysis of mobile service order performance and trends.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[CCDW.SERVICE_PROVIDER]]
- ← [[CLM_CCM.V_CCM_DEALER_DIM]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CLM_KIM.V_REALTIME_GOODIES]]


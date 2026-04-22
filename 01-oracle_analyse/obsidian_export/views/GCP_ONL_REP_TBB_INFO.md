# GCP_ONL_REP_TBB_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'GCP_ONL_REP_TBB_INFO' (likely for 'GCP Online Report Trådløst Bredbånd Info'), provides a consolidated report of new service orders for Fixed Wireless Access (FWA) or Home Mobile Broadband products, specifically excluding business customers. It combines general service order details, specific product parameters (like IMSI), subscribed offer information, and customer/delivery contact parameters (such as owner/user IDs, contact phone, email, delivery address). The purpose is to offer a comprehensive dataset for analyzing or reporting on these specific broadband service orders.

## Data Sources (Inputs)
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]


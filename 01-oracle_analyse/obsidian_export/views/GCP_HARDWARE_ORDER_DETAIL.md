# GCP_HARDWARE_ORDER_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates comprehensive detailed information about hardware orders placed through Telenor's online store (`telenor.no`). It enriches core hardware order data with product specifics (e.g., GTIN, IMEI, material categories, manufacturer, model, color, size), payment and shipping details (price, method, delivery operator), service order information (subscription POIDs, monthly prices, product names, market products, actions, statuses, churn days), agreement details (SWAP, Insurance, Downpayment, including POIDs, product names, monthly prices, and churn days, along with discounts), and extensive customer demographic data (ID, name, age, age group, address, postal code, municipality, county). The primary purpose is to provide a unified and detailed dataset for analytical reporting, sales performance tracking, customer behavior analysis, and product analysis related to online hardware sales, specifically prepared for loading into a data analytics platform (Viya).

## Data Sources (Inputs)
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT]]
- ← [[CCM.GCP_PRODUCT_DIM_SUBS_PRICE_ADJ]]
- ← [[ONL_REP.SERVICE_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[CM.CUSTOMER]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[GALAXY.HANDSET_DIM_V]]
- ← [[CM.SUBSCRIPTION]]


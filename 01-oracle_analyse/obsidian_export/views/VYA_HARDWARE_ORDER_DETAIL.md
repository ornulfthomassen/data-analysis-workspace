# VYA_HARDWARE_ORDER_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYA_HARDWARE_ORDER_DETAIL`, provides a comprehensive and detailed overview of hardware orders, primarily for Telenor's online store ('telenor.no'). It integrates data from various sources to produce detailed order line information, including hardware specifics (IMEI, GTIN, manufacturer, model, color), sales and return KPIs, subscription details (POID, churn days, monthly price, product names), service order and agreement order status and actions, customer demographics (age, postal code, municipality), and market area information. It also classifies sales into a 'SALES_MATRIX' indicating new sales, upsell, downsell, or other categories. The view is designed to load hardware order data into a Viya analytics platform.

## Data Sources (Inputs)
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
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


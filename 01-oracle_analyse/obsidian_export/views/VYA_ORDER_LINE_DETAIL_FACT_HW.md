# VYA_ORDER_LINE_DETAIL_FACT_HW

**Schema:** `CCM` | **Type:** `View`

## Description
This view constructs a detailed fact table of hardware order lines, enriching raw hardware order data with dimensional attributes from various sources. It calculates sales-related Key Performance Indicators (KPIs) such as new sales, gross sales, and device-specific sales, considering different order types (standard and returns). The primary purpose is to provide a comprehensive dataset for analytical reporting and data warehousing, specifically for hardware orders from online channels ('Nettbutikken telenor.no').

## Data Sources (Inputs)
- ← [[ONL_REP.MOOA_ORDER_LINK]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT]]
- ← [[FPS.TERMINAL_GTIN]]
- ← [[ONL_HW_ORDERS_REP.HARDWARE_ORDER_PRODUCT_PARAM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CM.CUSTOMER]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]


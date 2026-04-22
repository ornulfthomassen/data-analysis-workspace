# DELV_ORDER_DETAIL_FACT

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed order line information with various dimensional attributes (product, order status, dealer, customer, dates, market areas) to create a comprehensive analytical dataset. It calculates several Key Performance Indicators (KPIs) related to sales (newsale, product change, porting, gross sale, termination) and includes a sophisticated 'SALES_MATRIX' classification (e.g., Upsale, Downsale, Newsale, Neutrale, Crossbrand) based on product type hierarchies. The view aims to provide a granular fact table for analyzing sales performance, order status, and customer behavior related to product changes, filtered for data from January 1, 2014, onwards.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[GALAXY.SUBSCR_OWNER_DIM_V]]
- ← [[GALAXY.CUSTOMER_SEGMENT_OWNER_DIM_V]]
- ← [[GALAXY.ORDER_STATUS_DT_DIM_V]]
- ← [[GALAXY.MARKET_AREA_DIM]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.MARKET_AREA_FROM_V]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[CLM_CCM.CCM_CUSTOMER]]


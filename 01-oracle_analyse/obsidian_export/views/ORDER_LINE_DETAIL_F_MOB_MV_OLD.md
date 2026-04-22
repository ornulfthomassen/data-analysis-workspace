# ORDER_LINE_DETAIL_F_MOB_MV_OLD

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive and consolidated analytical dataset for mobile order lines, focusing on specific business and market areas. It integrates data from various dimensions (dates, products, dealers, service providers, customers, campaigns, segments) to enrich raw order line details. The view calculates numerous Key Performance Indicators (KPIs) related to sales (e.g., newsale, gross sale, upsale, downsale, product change, swap), porting (inbound/outbound), and termination. It also includes business logic for classifying sales types ('SALES_MATRIX'), tracking specific product offerings ('Familiebonus', 'Datakontroll'), and providing insights into regretted orders and previous order context. Its purpose is to support in-depth CRM, sales performance, and churn/retention analysis for mobile services.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[GALAXY.SUBSCR_USER_LOC_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.ORDER_CATEGORY_DIM]]
- ← [[CCDW.SERVICE_PROVIDER]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.segment_dim_v]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]


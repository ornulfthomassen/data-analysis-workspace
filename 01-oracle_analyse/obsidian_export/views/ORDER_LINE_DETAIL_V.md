# ORDER_LINE_DETAIL_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "ORDER_LINE_DETAIL_V", serves as a comprehensive analytical dataset providing detailed information about individual order lines. It integrates data from various dimensions (dates, products, customers, dealers, campaigns, service providers, binding, source systems) with core order line facts. The view applies complex business logic to derive crucial analytical dimensions such as sales matrix classifications (upsale, downsale, newsale), retail groups, sales channels, and customer segmentation attributes (profit segment, MAP2, CLM Livsfase). It also calculates numerous key performance indicators (KPIs) related to sales (new sales, gross sales, including speech-specific versions), product changes, porting activities (inbound, outbound, speech, MBB specific), and terminations. The data is filtered for a specific business area (BUSINESS_AREA_KEY = 2) and recent order status years (2017, 2018), excluding cancelled orders, making it suitable for detailed operational and strategic analysis of order lines and associated customer/sales activities.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.SOURCE_SYSTEM_DIM_V]]
- ← [[CRM_ANALYSE.KIM_SERVICE_PROVIDER_DIM_V]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]
- ← [[CRM_ANALYSE.PROFITSEGMENT_MOBILE]]
- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]


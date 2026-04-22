# TEST_ORDER_1_DAY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`TEST_ORDER_1_DAY_V`) provides a comprehensive analytical dataset focused on mobile order lines. It integrates detailed information about orders, products (both 'to' and 'from' products for changes), customer demographics, household data, sales channels, dealer specifics, campaign treatments, and various key performance indicators (KPIs) such as newsale, terminations, porting (inbound/outbound), gross sale, and product changes. The data is filtered for specific business areas ('MOBILE'), market segments ('Privat'), and order statuses, primarily focusing on 'final booked' orders or specific porting-out scenarios. It enriches the core order data with geographical information, age groups, and other customer attributes, making it suitable for detailed reporting and analysis of customer behavior, product performance, and sales channel effectiveness.

## Data Sources (Inputs)
- ← [[galaxy.order_line_detail_fact_mv]]
- ← [[galaxy.product_dim]]
- ← [[galaxy.binding_type_benefit_dim]]
- ← [[galaxy.dealer_dim]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER_T]]
- ← [[CRM_ANALYSE.DIMPOSTNUMMER]]
- ← [[galaxy.business_area_dim_v]]
- ← [[galaxy.order_line_type_dim]]
- ← [[galaxy.market_area_dim]]
- ← [[galaxy.order_status_dim_mv]]
- ← [[galaxy.handset_dim_v]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[CCM.CCM_CUSTOMER]]
- ← [[CRM_ANALYSE.HOUSEHOLD_LAT_LONG_SHOP_V]]
- ← [[GALAXY.BINDING_PRODUCT_DIM_V]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[GALAXY.CAMPAIGN_HIT_TYPE_DIM]]
- ← [[CRM_ANALYSE.BR_ANALYTIC_UNIVERSE_SUBSET]]
- ← [[CRM_ANALYSE.NRPORT_SERVICE_PROVIDER]]
- ← [[GALAXY.DATE_DIM_MV]]


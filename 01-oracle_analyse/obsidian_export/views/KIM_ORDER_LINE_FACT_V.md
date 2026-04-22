# KIM_ORDER_LINE_FACT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_ORDER_LINE_FACT_V`, provides a comprehensive analytical dataset focusing on order line details, enriching a core fact table with various dimensional attributes. Its primary purpose is to enable reporting and analysis related to sales, new acquisitions (KPI_NEWSALE), and product changes (KPI_PRODUCT_CHANGE). It filters orders based on specific market areas, order statuses (e.g., 101, likely 'completed'), and order line types, while excluding certain invalid order line status reasons. It also converts date/time keys into readable date and timestamp formats and includes customer household information.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.MARKET_AREA_DIM]]
- ← [[GALAXY.MARKET_AREA_FROM_V]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[GALAXY.ORDER_TIME_DIM_V]]
- ← [[GALAXY.BINDING_PRODUCT_DIM_V]]
- ← [[GALAXY.BINDING_TYPE_BENEFIT_DIM]]
- ← [[GALAXY.ORDER_LINE_TYPE_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


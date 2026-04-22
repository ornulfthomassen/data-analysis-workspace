# V_CHURN_DSL

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named 'V_CHURN_DSL', is designed for churn analysis, likely focusing on Digital Subscriber Line (DSL) or similar telecommunication services. It aggregates the total number of order lines (`NUMBER_OF_ORDER_LINES`) for specific products that are associated with termination, cancellation, or resale activities. The view joins a central `ORDER_DETAIL_FACT_V` table with numerous dimension tables (date, subscription, user, product, order indicators, order status, product category, owner, market area) to provide detailed contextual information for each aggregated record. Filters are applied to include specific product names (identified by numerical codes), customer order types (primarily 'OPPSIGELSE' - termination/cancellation, and 'VIDERESALG' - resale), an 'OPPSAGT' (cancelled/terminated) order action type, and an 'OPPDATERT' (updated) order status. It also excludes a specific product category ('FIBSVB') and certain business classifications, while restricting data to 'PRIVAT' (private) and 'PRIVAT BEDRIFT' (private business) market areas. The output provides a granular breakdown of these terminated/resale order lines by day, week, month, main number, user, product, and various order status and indicator descriptions.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_STATUS_DT_DIM_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
- ← [[GALAXY.SUBSCR_USER_DIM_V]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.SALES_ORDER_INDICATOR_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]
- ← [[GALAXY.ORDER_STATUS_REASON_DIM_V]]
- ← [[GALAXY.ORDER_DETAIL_FACT_V]]
- ← [[GALAXY.PRODUCT_CATEGORY_DIM_MV]]
- ← [[GALAXY.COUNTERPART_OWNER_DIM_V]]
- ← [[GALAXY.MARKET_AREA_DIM]]
- ← [[GALAXY.SUBSCR_OWNER_DIM_V]]


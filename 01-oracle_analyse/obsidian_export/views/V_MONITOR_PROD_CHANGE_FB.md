# V_MONITOR_PROD_CHANGE_FB

**Schema:** `CCM` | **Type:** `View`

## Description
This view monitors and analyzes product changes (upsales, downsales, or neutral changes) for mobile telephony subscriptions. It quantifies these changes using 'KPI_PRODUCT_CHANGE' and categorizes them by 'SALES_MATRIX'. A key aspect is the analysis of these product changes in relation to customers who have activated a 'Familiebonus' (family bonus) product/service, tracking the time elapsed ('DAYS_AFTER') since the 'Familiebonus' activation. The analysis is further broken down by sales channel and various date dimensions.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]


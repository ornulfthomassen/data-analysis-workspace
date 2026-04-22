# V_CCM_KURT_CHAIN_AFILIATION

**Schema:** `CCM` | **Type:** `View`

## Description
This view analyzes customer order data to determine customer-dealer chain affiliations and aggregate key performance indicators (KPIs) over the past two years. For each unique customer (identified by KURT_ID), it calculates the number of distinct dealer chains and IDs they have interacted with, the date and associated dealer information for their first and last orders (both general and specifically for 'terminal newsales' involving handsets). It also sums various KPIs such as bindings, newsales, porting inbound, product changes, terminations, and gross sales. The analysis is focused on voice subscription products sold through physical stores in specific market areas.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]


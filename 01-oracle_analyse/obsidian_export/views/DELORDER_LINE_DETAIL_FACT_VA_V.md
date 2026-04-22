# DELORDER_LINE_DETAIL_FACT_VA_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named DELORDER_LINE_DETAIL_FACT_VA_V, serves as a direct projection of the `order_line_Detail_fact_mv` materialized view. Its primary purpose is to expose detailed, factual information about individual order lines for analytical and reporting needs within the CRM_ANALYSE schema. It includes various keys for joining with dimension tables (e.g., ORDER_KEY, PRODUCT_CATEGORY_KEY, CUSTOMER_KEY, etc.) and specific measures (KPIs) related to sales activities (e.g., KPI_NEWSALE, KPI_TERMINATION, KPI_GROSS_SALE). Some character columns are explicitly cast to specific lengths.

## Data Sources (Inputs)
- ← [[galaxy.order_line_Detail_fact_mv]]


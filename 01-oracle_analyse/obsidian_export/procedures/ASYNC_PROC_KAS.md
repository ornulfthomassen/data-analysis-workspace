# ASYNC_PROC_KAS

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `ASYNC_PROC_KAS` procedure dynamically constructs and executes a `CREATE TABLE AS SELECT` statement. Its primary purpose is to create a new permanent table named `TMP_STOCK_FTV_HIST_RAW_KAS`. This table is populated with detailed historical subscription and product data, extracted from various GALAXY schema data warehouse tables and materialized views. The data is filtered for specific product categories (e.g., 'Bredbånd', 'Frihet', 'TV'), subscription statuses, and a given date (`V_DATO`), representing raw, denormalized subscription information for the 'KAS' source system.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[TMP_STOCK_FTV_HIST_RAW_KAS]]


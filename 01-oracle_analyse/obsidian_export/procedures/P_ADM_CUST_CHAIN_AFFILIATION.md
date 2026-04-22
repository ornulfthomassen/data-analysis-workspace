# P_ADM_CUST_CHAIN_AFFILIATION

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_CUST_CHAIN_AFFILIATION calculates and aggregates customer order and dealer chain affiliation metrics for a specified month (P_YYYYMM). It identifies customers' first and last dealer chain affiliations, various sales KPIs (e.g., newsale, binding, termination), and provides lists of associated order details and dealer chains. This aggregated data, spanning a 24-month lookback period, is initially processed and stored in a temporary table, which is then used to populate a specific monthly partition within a permanent 'ADM_CUSTOMER_CHAIN_AFFILIATION' table. The process includes checks for existing partitions, handling potential overwrites, and managing temporary table lifecycle.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_CHAIN_AFFILIATION]]
- → [[TMP_CUSTOMER_CHAIN_AFFILIATION]]


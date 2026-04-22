# P_ADM_DEVICE_AGREEMENT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_DEVICE_AGREEMENT`, processes and aggregates historical data related to device agreements, subscriptions, customers, and IMEI (device) usage for a specified month (`P_YYYYMM`). It constructs a complex SQL query to gather detailed information from various sources, including agreement details, product information, customer mappings, subscription history, and device usage records. The results are first inserted into a temporary staging table (`TMP_DEVICE_AGREEMENT`). Subsequently, this temporary table is used to exchange a partition within the main administrative table (`ADM_DEVICE_AGREEMENT`), effectively updating or inserting the monthly snapshot of device agreement data. The procedure handles partition creation, error logging, and statistics gathering.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[LIVE.SUBSCRIPTION_HANDSET_HIST]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]

## Target Tables (Outputs)
- → [[TMP_DEVICE_AGREEMENT]]
- → [[ADM_DEVICE_AGREEMENT]]


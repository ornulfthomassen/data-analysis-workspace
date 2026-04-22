# P_ADM_DEVICE_AGREEMENT_INACT_O

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_DEVICE_AGREEMENT_INACT_O`, extracts and processes detailed information related to device agreements (like SWAP agreements and insurance products), associated subscriptions, and IMEI data for a specific reporting month (`P_YYYYMM`). It calculates various statuses (e.g., agreement status, IMEI status, subscription status, subscription change type) based on validity dates. The main purpose is to build or update a historical snapshot of device agreements and their states. It achieves this by creating a temporary staging table, populating it with the extracted data, and then performing a partition exchange operation to load the data into a specific monthly partition of the permanent `ADM_DEVICE_AGREEMENT_INACTIVE` table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_HIST]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]

## Target Tables (Outputs)
- → [[TMP_DEVICE_AGREEMENT_INACTIVE]]
- → [[ADM_DEVICE_AGREEMENT_INACTIVE]]


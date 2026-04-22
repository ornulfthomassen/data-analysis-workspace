# P_ADM_AGREEMENT_DEVICE_ALL2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure creates and populates three permanent analytical tables related to device agreements: ADM_AGREEMENT_DEVICE, ADM_AGREEMENT_DEVICE_SWAP, and ADM_AGREEMENT_DEVICE_INSURANCE. It consolidates data from various source systems (e.g., GALAXY, CM, ONL_REP, CCDW, LIVE, CLM_ADM) to provide detailed insights into device agreements, their associated customer and subscription information, device IMEI details, and specific product offers like device swaps and insurance. The procedure dynamically drops existing versions of these tables, recreates them using `CREATE TABLE AS SELECT` statements, grants SELECT privileges to 'CRM_ANALYSE', and creates multiple indexes to optimize query performance for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE]]
- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]

## Target Tables (Outputs)
- → [[ADM_AGREEMENT_DEVICE]]
- → [[ADM_AGREEMENT_DEVICE_SWAP]]
- → [[ADM_AGREEMENT_DEVICE_INSURANCE]]


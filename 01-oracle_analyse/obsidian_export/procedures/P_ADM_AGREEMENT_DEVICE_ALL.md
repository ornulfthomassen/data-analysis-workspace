# P_ADM_AGREEMENT_DEVICE_ALL

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_AGREEMENT_DEVICE_ALL` creates and populates a new permanent table named `ADM_AGREEMENT_DEVICE_ALL` within the `CLM_ADM` schema. This table serves as a comprehensive data mart or analytical table, aggregating detailed information about customer agreements, associated devices (identified by IMEI), products, and subscriptions from various source systems. It consolidates data related to agreement statuses, product details, dealer information, subscription lifecycle events (e.g., port-ins, ownership changes), and device usage. The procedure also creates indexes on the new table, computes statistics, and grants select privileges to specific users/roles to optimize performance and access for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.AGREEMENT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_OFFER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]


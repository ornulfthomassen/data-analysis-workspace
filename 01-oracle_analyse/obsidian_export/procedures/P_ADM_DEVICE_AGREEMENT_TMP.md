# P_ADM_DEVICE_AGREEMENT_TMP

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_ADM_DEVICE_AGREEMENT_TMP` is designed to create or refresh a temporary table named `TMP_DEVICE_AGREEMENT`. This temporary table aggregates and processes comprehensive data related to device agreements for a specific month (identified by `P_YYYYMM`). It combines information from various sources, including agreement details, product specifications, status information, IMEI data, and subscription details, to provide a detailed view of device agreements and their lifecycle.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
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
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[LIVE.EUREKA_IMEI]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.PROD_SERV_MAPPING]]
- ← [[SYS.ALL_OBJECTS]]

## Target Tables (Outputs)
- → [[TMP_DEVICE_AGREEMENT]]


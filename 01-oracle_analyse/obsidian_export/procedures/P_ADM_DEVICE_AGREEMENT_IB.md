# P_ADM_DEVICE_AGREEMENT_IB

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_ADM_DEVICE_AGREEMENT_IB` is designed to fully refresh (drop and recreate) a data mart table named `ADM_DEVICE_AGREEMENT_IB` within the `CLM_ADM` schema. It populates this table with a comprehensive and consolidated view of device agreements, including related subscription details, customer information (owner and user), product data, IMEI (International Mobile Equipment Identity) details, and various status and date indicators. The procedure involves complex logic to categorize subscription change types, determine agreement statuses, and associate historical and current data from multiple source systems.

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
- → [[ADM_DEVICE_AGREEMENT_IB]]


# P_ADM_STOCK_AGREEMENT_DEVICE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_STOCK_AGREEMENT_DEVICE` creates or refreshes the `CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL` table. This table consolidates extensive information about customer agreements, subscriptions, product offers (specifically for devices, including 'SWAP' and 'Forsikring'), IMEI details, and their associated statuses and usage history. It denormalizes data from various source systems to provide a comprehensive view suitable for analytical or reporting purposes, focusing on device-related agreements and their lifecycle management.

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
- → [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]


# P_ADM_STOCK_AGREEMENT_DEVICE01

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure consolidates and processes detailed information about device-related agreements. It gathers data from various sources including agreement dimensions, agreement offers, product dimensions, product configurations (e.g., IMEI, parameters), service orders, subscription mappings, customer mappings, and IMEI usage data. The procedure calculates various status flags for products, devices, and subscriptions, extracts agreement terms (start/end dates, prices, termination fees), and links devices to subscriptions and customer information. The primary purpose is to create a comprehensive, denormalized view (materialized as a table) of device agreements, likely for administrative reporting, inventory management, or analytical purposes, focusing on agreement types like SWAP, insurance, and payment plans.

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
- → [[ADM_STOCK_AGREEMENT_DEVICE_V01]]


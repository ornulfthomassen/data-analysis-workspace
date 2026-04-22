# GCP_AGREEMENT_DEVICE_ALL

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "GCP_AGREEMENT_DEVICE_ALL", provides a comprehensive and aggregated overview of device agreements, primarily for 'SWAP' (device exchange) and 'Forsikring' (device insurance) products. It integrates data from various domains including agreement details, device specifications (IMEI, manufacturer, model), customer information (owner and user demographics, lifecycle segments, communication preferences), subscription data (order and usage, status, port-out details), product information, and dealer/sales channel data. The view calculates numerous key performance indicators (KPIs) related to swap, insurance, duration, and subscription port-outs. It also derives complex agreement statuses and phases, with specific logic differentiating between swap and insurance product lifecycles and durations. The overall purpose is to consolidate and enrich disparate data points into a single analytical dataset for reporting and analysis of device agreements and their associated entities.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_TRANSFER]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_SWAPPED]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
- ← [[CLM_ADM.ADM_AGREEMENT_MEMB_INSURANCE_V]]
- ← [[CLM_ADM.ADM_AGREEMENT_MEMB_SWAP_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[THIRD_PARTY_SERVICES.HANDSET_GTIN]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]


# VYA_ADM_AGREEMENT_DEVICE_ALL

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ADM_AGREEMENT_DEVICE_ALL, consolidates comprehensive data related to customer device agreements, with a specific focus on 'SWAP' (device exchange) and 'FORSIKRING' (device insurance) products. It calculates numerous Key Performance Indicators (KPIs) such as swap activity, insurance status, and duration-based metrics. The view enriches agreement details with information about the associated devices (IMEI, manufacturer, specifications), customer demographics (age, gender, marketing preferences, lifecycle segments for both owner and user), subscription order and usage history (status, product names, port-in/out details), and dealer information. It determines complex agreement statuses and phases, adjusting start/end dates for accurate duration analysis. The primary purpose is to provide a detailed, analytical dataset for tracking and evaluating the lifecycle, performance, and customer engagement for device-related agreements.

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


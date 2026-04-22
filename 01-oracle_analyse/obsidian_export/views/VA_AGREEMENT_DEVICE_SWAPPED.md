# VA_AGREEMENT_DEVICE_SWAPPED

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view is designed to analyze device and agreement swap events. It captures comprehensive details for both the 'from' (original) agreement/device and the 'to' (new/swapped) agreement/device, linking them based on swap matching criteria. It includes information on agreement status, device specifications, customer demographics, and subscription details, allowing for detailed reporting and analysis of device swap processes and their impact on customers and services.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_SWAPPED]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CLM_ADM.ADM_AGREEMENT_MEMB_INSURANCE_V]]
- ← [[CLM_ADM.ADM_AGREEMENT_MEMB_SWAP_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[THIRD_PARTY_SERVICES.HANDSET_GTIN]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]


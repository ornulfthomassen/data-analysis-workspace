# VYA_AGREEMENT_DEVICE_SWAPPED

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a detailed, combined dataset of original and swapped product agreements, devices, customers, and subscriptions, specifically for device swap events, intended as a data source for 'Mjøsa' (a data warehouse/BI system). It tracks agreement status, device details, customer demographics, and subscription information for both the 'from' and 'to' parts of a device swap.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_SWAPPED]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CLM_ADM.ADM_AGREEMENT_MEMB_INSURANCE_V]]
- ← [[CLM_ADM.ADM_AGREEMENT_MEMB_SWAP_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
- ← [[THIRD_PARTY_SERVICES.HANDSET_GTIN]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]


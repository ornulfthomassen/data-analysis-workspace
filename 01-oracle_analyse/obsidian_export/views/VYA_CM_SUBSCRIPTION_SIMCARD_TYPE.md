# VYA_CM_SUBSCRIPTION_SIMCARD_TYPE

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and de-duplicates subscription and SIM card related information, including ICC_ID, IMSI_NUMBER, product details, and validity periods. It filters out specific product offers (likely related to barring or auxiliary services) and prioritizes data from various sources to create a consistent record. The primary purpose is to provide cleansed and enriched subscription SIM card type data for loading into a data warehouse system referred to as 'MJØSA'. It includes specific logic for 'MAINCARD' type subscriptions and handles historical validity using a LAG function.

## Data Sources (Inputs)
- ← [[SIMNR.SIMCARD_DETAILS]]
- ← [[CM.REL_NUMBER]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.SUBSCRIPTION_EQUIPMENT_INFO]]


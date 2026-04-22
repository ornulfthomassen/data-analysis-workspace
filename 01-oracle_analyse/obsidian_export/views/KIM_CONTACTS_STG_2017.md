# KIM_CONTACTS_STG_2017

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and enriches contact history records for the year 2017 by joining them with customer mapping, treatment characteristics, product dimensions, and subscription master data. It creates a comprehensive staging dataset of contact events, providing detailed information about the event itself, associated campaigns, channels, products, and customer subscriptions, preparing this data for further analysis or reporting.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACT_HIST_2017]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


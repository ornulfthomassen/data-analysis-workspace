# KIM_CONTACTS_STG_2019

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'KIM_CONTACTS_STG_2019', consolidates and enriches contact history records for the year 2019. It combines data from various sources including contact history, customer mapping, treatment characteristics (both character and numeric UDFs), product dimensions, and subscription master data. The view aims to create a comprehensive, denormalized staging dataset with detailed information about each contact event, including associated campaign, product, customer, and subscription details, along with various derived attributes like event week/month and unique identifiers.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACT_HIST_2019]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


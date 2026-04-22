# KIM_CONTACTS_STG_2018

**Schema:** `CCM` | **Type:** `View`

## Description
The view 'KIM_CONTACTS_STG_2018' serves as a staging area for consolidated contact history data for the year 2018. It combines primary contact records with detailed information about customer mappings, campaign treatments (including both character and numeric user-defined fields), product attributes, and subscription master data. The purpose is to enrich raw contact events with various contextual dimensions, preparing a comprehensive dataset for further analysis or loading into a data warehouse for marketing campaign performance tracking or customer interaction analytics.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACT_HIST_2018]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


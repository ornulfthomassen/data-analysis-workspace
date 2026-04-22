# KIM_CONTACTS_STG_2020

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, denormalized dataset of customer contact history for the year 2020. It combines core contact records with detailed information from various related entities such as campaigns, activities, products, customer subscriptions, and treatment characteristics (both character-based and numeric user-defined fields). The view's purpose is to enrich contact data, likely for reporting, analytics, or as a staging area for further data processing, presenting a 360-degree view of each customer interaction with associated contextual information.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACT_HIST_2020]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


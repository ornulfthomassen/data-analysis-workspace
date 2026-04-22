# VYAMN_CONTACTS_STG

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYAMN_CONTACTS_STG`, serves as a staging area to prepare a comprehensive and enriched dataset of customer contact events ('contracts') for a new data loading process, explicitly without using Hive. It integrates various customer interaction, campaign, product, and subscription-related attributes from multiple source systems, performing data transformations, consolidations (e.g., using COALESCE), and lookups to create a unified view of these contact events for further analytical processing or loading into a data warehouse.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACTS_STG_DV]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CDM.CI_SUBS_CONTACT_HISTORY]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_CDM.CI_CHANNEL]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


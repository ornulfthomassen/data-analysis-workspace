# KIM_CONTACTS_STAGE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view serves as a staging or integration point for customer contact events. It consolidates raw contact data with detailed information from various sources including customer mappings, dynamic treatment attributes, campaign characteristics, product dimensions, and subscription history. The purpose is to enrich contact records, providing a comprehensive view of each interaction event with associated campaign, product, and customer context, suitable for further analytical processing or loading into a data warehouse. It also handles data type conversions and null value management for consistency.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACTS_STG_DV]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


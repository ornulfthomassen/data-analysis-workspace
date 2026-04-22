# KIM_CONTACTS_STG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates customer contact event data by joining core contact records with associated campaign details, product information, customer and subscription identifiers, and treatment characteristics from various source and dimensional tables. Its purpose is to create a comprehensive, de-normalized dataset of customer interactions/events, suitable for reporting, analysis, or further data warehousing processes.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACTS_STG]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


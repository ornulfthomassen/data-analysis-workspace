# KIM_CONTACTS_HIST_STAGE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'KIM_CONTACTS_HIST_STAGE_V', serves as a comprehensive staging layer for historical customer contact data. It consolidates information from various sources related to customer interactions, campaigns, treatments, activities, products, and subscriptions. The view denormalizes and enriches raw contact records with detailed attributes such as event type, priority, date/time components (week, month), campaign details, channel information, product actions, customer flags, and treatment-related data (e.g., propensity). The 'DISTINCT' clause suggests it's designed to provide unique contact event records with all relevant contextual attributes, likely for analytical purposes such as campaign effectiveness analysis, customer journey mapping, or loading into a data warehouse.

## Data Sources (Inputs)
- ← [[CLM_KIM.KIM_CONTACT_HIST_2020]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_CDM.CI_DYNAMIC_TREATMENT_ATTRIBUTE]]
- ← [[CLM_KIM.CI_TREATMENT_CHAR_UDF_MRG_V]]
- ← [[CLM_CCM.PRODUCT_DIM_V]]
- ← [[CLM_KIM.CI_TREATMENT_NUM_UDF_V]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


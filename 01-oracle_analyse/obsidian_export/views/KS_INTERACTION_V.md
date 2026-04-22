# KS_INTERACTION_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, denormalized record of customer interactions and their segments. It consolidates various attributes such as interaction timings, durations, agent details, queue information, media type, and specific interaction results. It also enriches the interaction data by mapping 'owner' and 'user' identifiers (KURT_ID) from the base interaction table to a standardized customer master key (CUSTOMER_SK) using the customer mapping table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KS_INTERACTION]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]


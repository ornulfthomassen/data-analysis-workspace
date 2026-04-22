# VYA_CCM_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_CCM_CUSTOMER, is designed to consolidate, enrich, and standardize comprehensive customer data for loading into a data platform (referred to as 'Mjøsa'). It combines basic customer information, demographic details (age and gender), household affiliations, and communication preferences (direct marketing, telemarketing, email, SMS consent/reservation statuses) from various source systems. Key transformations include generating anonymous household SKs for customers without a mapped household, categorizing age into age groups, and translating numerical consent indicators into descriptive text.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_MAPPING_V]]
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]


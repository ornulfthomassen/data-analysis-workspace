# VYA_CUSTOMER_HOUSEHOLD_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive aggregated overview of customer household information. It calculates various demographic statistics (like minimum, maximum, median, and average age; counts of individuals within specific age ranges and by gender) for each household. It also includes geographic details (municipality, postal code, housing type) and flags for different services (e.g., fixed telephony, TV, internet types) associated with the household, linked to a customer surrogate key.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_CUSTOMER_CONTACT_INFO]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


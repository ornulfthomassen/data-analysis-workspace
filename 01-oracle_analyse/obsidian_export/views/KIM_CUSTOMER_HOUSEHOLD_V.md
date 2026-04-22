# KIM_CUSTOMER_HOUSEHOLD_V

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a view that combines customer household and customer IDs from the 'CCM_CUSTOMER' table with an additional placeholder row where both IDs are -1. This placeholder row is often used to represent a 'None' or 'Not Applicable' option in user interfaces.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[CLM_CCM.CCM_CUSTOMER]]


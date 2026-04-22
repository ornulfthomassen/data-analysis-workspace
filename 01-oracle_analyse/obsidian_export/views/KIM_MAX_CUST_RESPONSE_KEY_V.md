# KIM_MAX_CUST_RESPONSE_KEY_V

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the maximum 'CUST_RESPONSE_KEY' from the 'KIM_CUSTOMER_RESPONSE' table, excluding records where 'source_system_key' is 94. If no such key is found, it defaults to 0. This is typically used to identify the highest existing customer response identifier.

## Data Sources (Inputs)
- ← [[KIM_CUSTOMER_RESPONSE]]


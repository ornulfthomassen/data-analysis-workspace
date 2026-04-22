# CI_CUST_CONTACT_HISTORY2_FIX

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `CI_CUST_CONTACT_HISTORY2_FIX` in the `CCM` schema, primarily serves as a wrapper or a 'fixed' version of another object with the exact same name located in the `clm_kim` schema. Its main function is to expose customer contact history data, performing explicit `CAST` operations on several key identifier columns (like `CUSTOMER_SK`, `SOURCE_SUBSCRIPTION_ID`, `MAIN_NUMBER_SK`, `SUBSCRIPTION_ID`, `OB_SUBSCRIPTION_ID`) to `VARCHAR` data types. This suggests a purpose of data type standardization, potentially for consistency or integration with other systems, without altering the core data or performing complex aggregations or joins.

## Data Sources (Inputs)
- ← [[clm_kim.CI_CUST_CONTACT_HISTORY2_FIX]]


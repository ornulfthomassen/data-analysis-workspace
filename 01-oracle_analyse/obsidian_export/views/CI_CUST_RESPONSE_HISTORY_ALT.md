# CI_CUST_RESPONSE_HISTORY_ALT

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a direct projection of customer response history data. Its primary function is to wrap the underlying `CI_CUST_RESPONSE_HISTORY_H1` source, casting several key identifier columns (like CUSTOMER_SK, REGARDING_MSISDN, MAIN_NUMBER_SK, SUBSCRIPTION_ID, CELL_PACKAGE_SK, TREATMENT_SK) to specific data types (VARCHAR or NUMBER) for consistency or specific application requirements.

## Data Sources (Inputs)
- ← [[clm_kim.CI_CUST_RESPONSE_HISTORY_H1]]


# CI_CUST_RESPONSE_HISTORY_ALT2

**Schema:** `CCM` | **Type:** `View`

## Description
The view `CI_CUST_RESPONSE_HISTORY_ALT2` serves as a direct projection of the `CI_CUST_RESPONSE_HISTORY_H2` data, making available a comprehensive history of customer responses, campaign activities, and related details. Its primary purpose is to present this data with specific data type conversions applied to several identifier columns (e.g., CUSTOMER_SK, REGARDING_MSISDN, SUBSCRIPTION_ID, CELL_PACKAGE_SK, TREATMENT_SK) to ensure consistency or compatibility for downstream applications, without adding complex filtering or aggregation logic. The 'ALT2' in its name suggests it might be an alternative or a specific version of a standard customer response history view.

## Data Sources (Inputs)
- ← [[clm_kim.CI_CUST_RESPONSE_HISTORY_H2]]


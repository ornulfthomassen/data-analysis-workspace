# VYL_SUBSCRIPTION_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a filtered and type-casted snapshot of subscription history details, including customer, product, market area, business area, and various activity duration metrics. The data is specifically filtered for a single historical month, which is dynamically calculated based on the current system date (5 days prior to one month ago). It appears to standardize data types by casting many fields to CHAR for reporting or integration purposes.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]


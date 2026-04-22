# GCP_ADM_SUBSCRIPTION_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'GCP_ADM_SUBSCRIPTION_AGG', serves as a direct projection or alias of the 'ADM_SUBSCRIPTION_AGG' data source. It exposes pre-aggregated subscription-related metrics including data usage (MB), MMS/SMS counts and costs (KR), speech duration and numbers, and various gross/net financial fees (e.g., periodic, initiation, termination, usage, discounts). The 'PREV1', 'PREV2', 'PREV3' suffixes on many columns suggest that these metrics represent data from previous periods (e.g., previous 1, 2, or 3 months). The view itself does not perform any new aggregations or transformations, but rather provides a specific access point or logical layer for this pre-existing aggregated subscription data.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]


# KIM_SUBSCRIPTION_STATUS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts the latest status (end date and associated product offer ID) for primary subscriptions. It filters out subscriptions from specific source systems (Marius, Pandora, K2) and includes only subscriptions from business areas 1 and 2, ensuring that only top-level, valid subscriptions are considered.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]


# GCP_SECURITY_SUBSCRIPTION_USE_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates security subscription usage metrics for each customer. It counts the occurrences of three specific security-related actions: email verification for ID monitoring, adding a monitored credit card, and creating a VPN token. Additionally, for each customer and each of these three actions, it identifies the earliest and latest recorded 'first_date' and 'last_date' associated with those actions.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_CCM_AGRM_SFTY_USE]]


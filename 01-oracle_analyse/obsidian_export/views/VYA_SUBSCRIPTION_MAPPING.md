# VYA_SUBSCRIPTION_MAPPING

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive mapping of subscription lifecycle and historical data. It extracts detailed attributes for customer subscriptions, including their current and previous states, start/end dates, product groups, market areas, and porting information. The data is filtered to include only subscriptions that are linked to a historical record whose end date falls within the last two years, indicating a focus on recently active or recently historical subscriptions.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]


# VYA_SUBSCRIPTION_TWIN_MAPPING

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and maps related or 'twin' subscriptions by linking child subscriptions to their parent subscriptions. It filters out self-referencing subscriptions (`parent_subscription_id <> subscription_id`) and applies additional criteria for specific business areas (ID 2), market areas (IDs 2, 3, 4), and a specific end date range (between April 1, 2019, and June 1, 2020). For each unique combination of parent subscription ID, child subscription ID, main number, and product name, it calculates the earliest start date and the latest end date among the aggregated records. The output provides a structured overview of these filtered and aggregated subscription relationships along with their associated product details and relevant timeframes.

## Data Sources (Inputs)
- ← [[ccdw.subscription]]
- ← [[pd]]


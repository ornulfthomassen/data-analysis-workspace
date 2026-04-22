# OS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named 'OS', provides a consolidated and summarized perspective on product subscriptions. It joins subscription details, subscribed offer details, and product information to present a single aggregated record for each unique combination of product name, subscription ID, and main number. Key information extracted includes product name, product key, subscription ID, main number, original and current start dates, market area, and customer IDs categorized by their role (owner, payer, user). It essentially creates a flattened view of subscriptions with associated product and customer role information.

## Data Sources (Inputs)
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[ODS.SUBSCRIBED_OFFER_ODS_MOB]]
- ← [[PD]]


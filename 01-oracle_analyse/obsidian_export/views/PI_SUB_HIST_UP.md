# PI_SUB_HIST_UP

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and retrieves key details (subscription key, source product ID, primary product start and end date keys) for specific mobile telephony subscriptions. It filters for subscriptions with a quantity of 1, primary products ending on or after January 1, 2022, from market areas 2 or 4, and where the product is categorized as 'Abonnement' (Subscription), 'Tale' (Voice), 'Mobil Telefoni' (Mobile Telephony) from the 'Pacman' source system, with a paytype of 0 and primary product flag set to 1. Essentially, it extracts historical or current details for a specific set of mobile voice subscriptions.

## Data Sources (Inputs)
- ← [[galaxy.subscription_dim_mv]]
- ← [[galaxy.subscr_detail_fact]]
- ← [[galaxy.primary_product_dim_v]]


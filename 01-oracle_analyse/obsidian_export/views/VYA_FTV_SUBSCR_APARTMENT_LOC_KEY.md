# VYA_FTV_SUBSCR_APARTMENT_LOC_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies specific 'broadband' subscriptions (from the 'KAS' source system) that are linked to 'street' locations (where IS_APARTMENT = 0). It targets scenarios where the customer also has 'apartment' type broadband subscriptions at the same physical address, and all such 'apartment' subscriptions for that customer and address share a single, unique location key. The view's purpose is to associate these identified 'street' subscriptions with that unique 'apartment' location key.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.LOCATION_DIM]]


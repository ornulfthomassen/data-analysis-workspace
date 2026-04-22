# TST_FTV_LOCATION_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to identify and categorize subscription lifecycle events at a specific location, focusing on 'churn' (departure) and 'tilvekst' (growth/arrival) events. It analyzes changes in subscription attributes such as products, technology, value chain, and customer association between consecutive monthly periods. Key outcomes include identifying customer movements ('FLYTTING'), returning customers ('RETURNING'), and tracking technology migrations (e.g., Fiber to Coax, TBB to Fiber). It aggregates these events per subscription, location, and month, prioritizing 'FLYTTING' events.

## Data Sources (Inputs)
- ← [[CCM.SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.LOCATION_DIM]]


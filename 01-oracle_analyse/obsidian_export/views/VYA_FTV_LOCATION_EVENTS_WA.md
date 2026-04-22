# VYA_FTV_LOCATION_EVENTS_WA

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies, classifies, and tracks broadband subscription lifecycle events (e.g., churn, new subscriptions, customer moves, technology changes) at the user location level. It analyzes sequential subscription changes for a given location, categorizing them into various event types like 'churn', 'tilvekst' (growth/new), 'moving' (Flytting), and 'returning', along with technology transition types (e.g., Fiber to Fiber, TBB to Fiber). The view provides key details for these events, including duration between changes, and flags indicating same customer, subscription, technology, or event month.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.LOCATION_DIM]]


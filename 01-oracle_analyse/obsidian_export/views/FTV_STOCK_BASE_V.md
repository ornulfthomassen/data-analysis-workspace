# FTV_STOCK_BASE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes monthly changes (growth, churn, and net change) in broadband (BB) and TV subscriptions. It compares the state of subscriptions between consecutive months to determine opening and closing balances, and aggregates detailed churn and growth event types. The view provides product-level detail for these metrics, excluding certain product categories.

## Data Sources (Inputs)
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[CCM.FTV_STOCK_EVENTS_GCP]]
- ← [[CCM.FTV_LOCATION_EVENTS_GCP]]


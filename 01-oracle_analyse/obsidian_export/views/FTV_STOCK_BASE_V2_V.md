# FTV_STOCK_BASE_V2_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view tracks monthly changes (churn, growth, stability) in Broadband (BB) and Television (TV) subscriptions. It aggregates subscription data, identifies product combinations (e.g., BB Only, TV Only, Dualplay), and categorizes changes between periods based on various event types (e.g., VULA, build-out, migration between technologies like Coax to Fiber, moving, returning, short-term subscriptions). It provides a base dataset for analyzing subscriber movements and the composition of the subscriber base over time, comparing 'Opening Balance' (OB) and 'Closing Balance' (CB) states.

## Data Sources (Inputs)
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[CCM.FTV_STOCK_EVENTS_GCP]]
- ← [[CCM.FTV_LOCATION_EVENTS_GCP]]


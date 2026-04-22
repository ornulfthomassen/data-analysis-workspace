# FTV_LOCATION_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, FTV_LOCATION_EVENTS_V, identifies and categorizes significant events related to broadband and TV subscriptions at specific user locations on a monthly basis. It analyzes month-over-month changes to detect and classify events such as churn (disconnection), 'tilvekst' (new acquisition or growth), customer movements ('FLYTTING'), and returning customers. The view also tracks technology migrations (e.g., Fiber to Fiber, TBB to Fiber, Coax to TBB) and changes in value chain or dwelling unit types. It consolidates these events, providing details like the subscription key, event date, involved technologies, and flags indicating various types of changes (e.g., same customer, same technology). The final output prioritizes certain event types (like 'FLYTTING') when multiple events occur for the same subscription at the same location within a given month.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.LOCATION_DIM]]


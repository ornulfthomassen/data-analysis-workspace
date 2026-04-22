# KS_INTERACTION_ORDERMATCH_B2_V

**Schema:** `CCM` | **Type:** `View`

## Description
Combines customer interaction records with order line details, linking specific interactions (e.g., calls) to sales orders. The matching is performed based on a common 'keyed number' (likely a phone number) and by ensuring the order date falls within a defined time window relative to the interaction's start date. This view likely serves to analyze the relationship, impact, or sequence between customer interactions and associated sales activities.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ks_interaction]]
- ← [[CRM_ANALYSE.KS_ORDER_LINE_REP]]


# UPSALE_KS_INTERA_MAIN_NR_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines customer interaction data with sales order data to identify and analyze customer product change orders that occurred prior to a specific customer interaction. It specifically filters for orders marked as 'product change' and from a certain date onwards. The core purpose appears to be for upsell analysis, by linking customer interactions to their past product change history, potentially to understand triggers, outcomes, or future opportunities related to these interactions.

## Data Sources (Inputs)
- ← [[CLM_KIM.ORDER_LINE_REP]]
- ← [[CRM_ANALYSE.ks_interaction]]


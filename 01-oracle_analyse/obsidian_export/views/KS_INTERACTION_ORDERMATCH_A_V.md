# KS_INTERACTION_ORDERMATCH_A_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view joins customer interaction records with sales order line items. It links interactions to orders based on the employee who handled both the interaction and the order, and it specifically matches orders that occurred chronologically within or immediately after the interaction's time frame (between `START_CAL_DATE` and `START_CAL_DATE_NEXT`). The primary purpose is to provide an integrated dataset for analyzing the relationship between customer interactions and sales outcomes, especially for CRM analytical reporting.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ks_interaction]]
- ← [[CRM_ANALYSE.KS_ORDER_LINE_REP]]


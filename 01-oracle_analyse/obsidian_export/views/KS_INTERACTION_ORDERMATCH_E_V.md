# KS_INTERACTION_ORDERMATCH_E_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and retrieves order line data that has not been matched or processed by the 'KS_INTERACTION_ORDERMATCH_C_V' view. It selects a comprehensive set of order-related attributes from 'KS_ORDER_LINE_REP', while setting all interaction-specific attributes (like call duration, agent IDs, etc.) to NULL. This suggests it's designed to represent 'unmatched' or 'excluded' order lines within a broader data model that combines interaction and order information, effectively serving as one leg of a union operation where only order details are relevant. It also filters for orders placed on or after January 1, 2017.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KS_ORDER_LINE_REP]]
- ← [[KS_INTERACTION_ORDERMATCH_C_V]]


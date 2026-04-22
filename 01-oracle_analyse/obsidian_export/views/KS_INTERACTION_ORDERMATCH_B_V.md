# KS_INTERACTION_ORDERMATCH_B_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to match customer interactions with associated orders. It combines detailed interaction data (such as call duration, queue times, employee information, and interaction type) from the 'ks_interaction' table with order-specific information (like product details, sales KPIs, order status, and sales representative details) from the 'KS_ORDER_LINE_REP' table. The matching is performed based on a common 'KURT_ID' and ensures that the order date falls within the start and end calendar dates of the interaction. This allows for analysis of how customer interactions relate to or influence sales and order activities.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ks_interaction]]
- ← [[CRM_ANALYSE.KS_ORDER_LINE_REP]]


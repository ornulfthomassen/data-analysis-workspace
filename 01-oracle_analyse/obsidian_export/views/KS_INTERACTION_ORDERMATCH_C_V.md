# KS_INTERACTION_ORDERMATCH_C_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KS_INTERACTION_ORDERMATCH_C_V`, serves as a consolidated dataset for analyzing customer interactions and their associated order matching, sales performance indicators (KPIs), product details, and employee/queue metrics. It combines a wide array of detailed data points from three underlying source views using a UNION operation, suggesting it unifies similar data from different origins or categories (represented by 'A', 'B', and 'B2'). The comprehensive list of columns indicates its purpose is to provide a holistic view for in-depth analysis of the customer interaction and sales order lifecycle.

## Data Sources (Inputs)
- ← [[KS_INTERACTION_ORDERMATCH_A_V]]
- ← [[KS_INTERACTION_ORDERMATCH_B_V]]
- ← [[KS_INTERACTION_ORDERMATCH_B2_V]]


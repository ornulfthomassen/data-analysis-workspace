# V_ORDER_USER_AGE

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the age of the customer at the time of each order for every order line. It specifically determines the user's age in full years by comparing the order date with the customer's birth date.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_FACT_V]]
- ← [[GALAXY.CUSTOMER_DIM]]


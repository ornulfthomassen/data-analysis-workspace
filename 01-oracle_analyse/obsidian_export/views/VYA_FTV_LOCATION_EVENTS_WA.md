# VYA_FTV_LOCATION_EVENTS_WA

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes changes in broadband subscription events (churn, growth, technology changes, customer movements) over time at a user location level. It identifies transitions in technology (e.g., Fiber to Coax), value chain, and dwelling unit type, categorizing events like short-term changes ('KORTVARIG'), customer moves ('FLYTTING'), and returning customers. The view uses analytic functions to compare successive subscription states and aggregates these events on a monthly basis, prioritizing certain event types for final output.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
| Column Name |
|---|
| BB_SUBSCRIPTION_KEY |
| PERIOD_MONTH_KEY |
| P1_BB_PRODUCT_KEY |
| P2_BB_PRODUCT_KEY |
| P3_BB_PRODUCT_KEY |
| P4_BB_PRODUCT_KEY |
| P1_BB_PRIM_PRODUCT_KEY |
| P3_BB_PRIM_PRODUCT_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCR_FWA_LOC_KEY |
| SUBSCR_USER_LOC_KEY |
| SUBSCRIPTION_KEY |
| USER_CUSTOMER_KEY |
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
| Column Name |
|---|
| TECHNOLOGY |
| VALUECHAIN |
| DWELLING_UNIT_TYPE |
| PRODUCT_KEY |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| CURRENT_GEOGRAPHY_ID |
| IS_APARTMENT |
| NUMBER_OF_DWELLING_UNIT |


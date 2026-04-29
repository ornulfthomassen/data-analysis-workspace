# FTV_LOCATION_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes subscription events related to location, tracking churn and growth (tilvekst) of services across different technologies and value chains. It identifies customer movements, short-term subscriptions, and transitions between technologies (e.g., Fiber, TBB, Coax) based on changes in subscription status over consecutive periods for a given location, customer, or subscription. The view consolidates these events to provide a comprehensive record of service changes at a location.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| BB_SUBSCRIPTION_KEY |
| TV_SUBSCRIPTION_KEY |
| BB_SOURCE_SYSTEM |
| TV_TYPE |
| P3_BB_PRODUCT_KEY |
| P4_BB_PRODUCT_KEY |
| P3_TV_PRODUCT_KEY |
| P4_TV_PRODUCT_KEY |
| P3_BB_PRIM_PRODUCT_KEY |
| P4_BB_PRIM_PRODUCT_KEY |
| NUM_SUBS |
| RUN_DT_KEY |
- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| SUBSCR_FWA_LOC_KEY |
| SUBSCR_USER_LOC_KEY |
| USER_CUSTOMER_KEY |
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
| Column Name |
|---|
| PRODUCT_KEY |
| TECHNOLOGY |
| VALUECHAIN |
| DWELLING_UNIT_TYPE |
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| CURRENT_GEOGRAPHY_ID |
| IS_APARTMENT |
| NUMBER_OF_DWELLING_UNIT |


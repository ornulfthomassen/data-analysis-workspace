# TST_FTV_LOCATION_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes customer subscription events at specific geographical locations. It tracks 'churn' (cancellation/loss) and 'tilvekst' (acquisition/gain) events, analyzing changes in technology (e.g., Fiber, TBB, Coax), value chain, and dwelling unit types over time. The view calculates flags to indicate continuity or changes in customer, subscription, and technology aspects, measures the days between events, and aggregates these events on a monthly basis, prioritizing 'moving' events (FLYTTING) when multiple events occur within the same month and partition.

## Data Sources (Inputs)
- ← [[CCM.SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1]]
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
| USER_CUSTOMER_KEY |
| SUBSCR_FWA_LOC_KEY |
| SUBSCR_USER_LOC_KEY |
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


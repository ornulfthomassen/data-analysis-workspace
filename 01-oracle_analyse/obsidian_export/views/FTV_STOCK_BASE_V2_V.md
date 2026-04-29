# FTV_STOCK_BASE_V2_V

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the monthly changes and status of fixed-line broadband (BB) and TV subscriptions. It analyzes product combinations, technology migrations (e.g., COAX to FIBER), and various churn/acquisition (tilvekst) events by comparing current and previous period subscription data and integrating product and event details.

## Data Sources (Inputs)
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
| Column Name |
|---|
| PRODUCT_KEY |
| TECHNOLOGY |
| SUBSCRIPTION_TYPE |
| PRIMARY_PRODUCT_FLAG |
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
- ← [[CCM.FTV_STOCK_EVENTS_GCP]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| CHURN_VULA |
| TILVEKST_UTBYGGING |
| TILVEKST_OFFNET |
- ← [[CCM.FTV_LOCATION_EVENTS_GCP]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| VIEW_TYPE |
| FLYTTING |
| RETURNING |
| COAX_TO_FIBER |
| TBB_TO_FIBER |
| KORTVARIG |


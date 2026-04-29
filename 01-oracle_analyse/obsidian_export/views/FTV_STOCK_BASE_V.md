# FTV_STOCK_BASE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Analyzes monthly stock and flow of Broadband (BB) and TV subscriptions, calculating opening (P1/P2) and closing (P3/P4) balances for various product types, and deriving comprehensive growth, churn, and change metrics based on subscription and event data.

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
- ← [[DUAL]]
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


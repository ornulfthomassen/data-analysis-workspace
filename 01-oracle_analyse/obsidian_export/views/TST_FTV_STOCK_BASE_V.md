# TST_FTV_STOCK_BASE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates monthly opening and closing balances for Broadband (BB) and TV subscriptions, along with various aggregated metrics for subscription growth, churn, and net changes. It disaggregates these changes by different product keys (P1-P4 BB and TV, and primary BB products) and categorizes specific churn and growth events such as VULA, utbygging (expansion/build-out), offnet, flytting (relocation), return, migrations from COAX to FIBER or TBB to FIBER, and short-term contracts ('kortvarig'). Essentially, it provides a comprehensive monthly overview of subscription dynamics.

## Data Sources (Inputs)
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[CCM.SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1]]
- ← [[CCM.FTV_STOCK_EVENTS_GCP]]
- ← [[CCM.FTV_LOCATION_EVENTS_GCP]]


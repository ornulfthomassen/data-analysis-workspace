# FTV_STOCK_EVENTS_FIX_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes monthly subscription 'stock events' such as churn and new growth. It does this by analyzing changes in broadband subscription product keys between consecutive months, correlating churn events with data from the VULA system, and classifying new growth events ('TILVEKST_UTBYGGING', 'TILVEKST_OFFNET') based on associated product details. The final output pivots these event types into distinct columns, providing counts of each event per period and subscription.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.VYA_FTV_MISSING_FAR_ID]]
- ← [[VULA.LOAD_VULA_WEB]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]


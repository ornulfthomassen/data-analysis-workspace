# VYA_FTV_STOCK_EVENTS_EXTRA

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes specific subscription events, namely 'CHURN_VULA' (churn events linked to VULA processes), 'TILVEKST_UTBYGGING' (new subscriptions related to network expansion), and 'TILVEKST_OFFNET' (new subscriptions categorized as off-net). It aggregates these events by month and subscription key, providing a count for each event type. The view aims to track and quantify different types of subscription status changes over time.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.VYA_FTV_MISSING_FAR_ID]]
- ← [[VULA.LOAD_VULA_WEB]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]


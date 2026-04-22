# TST_FTV_STOCK_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes monthly subscription stock events, specifically churn (CHURN_VULA) and new subscriptions (TILVEKST_UTBYGGING, TILVEKST_OFFNET). It determines churn by identifying subscriptions present in a previous month but not the current month, and then linking them to VULA (Virtual Unbundled Local Access) records. It identifies new subscriptions by finding those present in the current month but not the previous month, and then linking them to product activation details. The results are aggregated monthly for each subscription, counting the occurrences of these specific event types.

## Data Sources (Inputs)
- ← [[CCM.SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.VYA_FTV_MISSING_FAR_ID]]
- ← [[VULA.LOAD_VULA_WEB]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]


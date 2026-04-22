# FTV_STOCK_EVENTS_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and categorizes key monthly events for broadband and TV subscriptions. It focuses on detecting subscription churn (specifically 'CHURN_VULA' linked to VULA processes) and new activations or growth ('TILVEKST_UTBYGGING' for build-out related, 'TILVEKST_OFFNET' for off-net related). For each subscription and month, it provides flags (0 or 1) for these event types and an 'EXTRA_01' column containing a VULA ID for churn events or a Product Key for activation events, offering additional context.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.VYA_FTV_MISSING_FAR_ID]]
- ← [[VULA.LOAD_VULA_WEB]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]


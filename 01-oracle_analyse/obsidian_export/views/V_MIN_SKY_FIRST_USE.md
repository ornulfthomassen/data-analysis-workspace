# V_MIN_SKY_FIRST_USE

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies the initial activation (first usage event) of 'Min Sky Service' for various customer subscriptions. It calculates the number of days elapsed since this first activation and provides associated subscription details, user identifiers, and market/business area information. The view consolidates data from two different pathways to identify these activations and link them to subscriptions.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]


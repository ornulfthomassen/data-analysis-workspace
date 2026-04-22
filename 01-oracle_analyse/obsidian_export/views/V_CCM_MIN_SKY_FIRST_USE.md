# V_CCM_MIN_SKY_FIRST_USE

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies the earliest usage event for 'Min Sky' (or similar 'CMO-STO%' SKUs) services across different types of subscriptions. It then calculates the number of days that have passed since this first usage event until the current date for each relevant subscription. The logic is split into two main branches (united by UNION ALL), likely to cover different data flows or types of subscriptions (e.g., mobile vs. VDSL as hinted in comments).

## Data Sources (Inputs)
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[COMOYO.COMOYO_SUB_GRANT_EVENTS]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]


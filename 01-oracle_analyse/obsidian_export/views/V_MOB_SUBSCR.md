# V_MOB_SUBSCR

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves comprehensive details about active mobile subscriptions, including product information, subscription types, subscriber identification (owner, user, payer), market area, and associated binding/contract terms (start/end dates, product, type). It combines data from various operational and configuration tables.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]


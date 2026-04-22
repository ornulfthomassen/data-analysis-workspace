# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and reconciles Broadband (BB) and Television (TV) subscription data across various source systems and product types for the current and previous months. It identifies and associates BB and TV products (including primary products) for individual subscriptions, distinguishes between main consumer products and business products, and captures details like source system and Lumino-specific dual-play correlations. The view provides a monthly snapshot of active BB and TV subscriptions for reporting and analysis.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[KAS.KUNDE]]
- ← [[KAS.ABONNENTNR_MSISDN]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[CCDW.SUBSCRIBED_PRODUCT_FTV_EXT]]


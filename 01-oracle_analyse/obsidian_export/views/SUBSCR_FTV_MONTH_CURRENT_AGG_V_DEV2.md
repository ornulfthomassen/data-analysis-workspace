# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV2

**Schema:** `CCM` | **Type:** `View`

## Description
The view consolidates and aggregates detailed subscription and product information for fixed broadband (BB) and fixed TV (TV) services. It captures various product keys (primary and standard) for each subscription across four specific temporal periods (P1-P4, representing date boundaries around the current month). It includes specialized logic to identify and correlate Lumino TV and BB subscriptions, excludes specific 'TBB' TV subscriptions from the 'KAS' source system, and processes 'business' TV products separately. The main purpose is to provide a comprehensive, time-aware dataset of active BB and TV subscriptions, their product configurations, and source systems for reporting and analytical purposes, focusing on monthly aggregation.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[KAS.KUNDE]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[KAS.ABONNENTNR_MSISDN]]
- ← [[CCDW.SUBSCRIBED_PRODUCT_FTV_EXT]]


# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV_3

**Schema:** `CCM` | **Type:** `View`

## Description
This Oracle SQL view aggregates and tracks active fixed broadband (BB) and fixed TV (FTV) subscriptions on a monthly basis. It covers the current month and the upcoming month, providing a snapshot of the subscriber base. The view consolidates subscription details such as subscription keys, primary and sub-product keys, source systems, user location keys, and TV service types. It incorporates complex logic to identify the primary product within subscription bundles, handles specific customer segments (e.g., 'Lumino' dual-play services where both BB and TV are linked by location/customer, and exclusions for 'TBB' TV subscriptions), and processes both consumer and business (BED) subscriptions. The primary purpose is to deliver a comprehensive, aggregated view of the active fixed subscription base for reporting and analytical purposes, showing changes in active products over specific periods (P1 to P4).

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[KAS.KUNDE]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[KAS.ABONNENTNR_MSISDN]]
- ← [[CCDW.SUBSCRIBED_PRODUCT_FTV_EXT]]


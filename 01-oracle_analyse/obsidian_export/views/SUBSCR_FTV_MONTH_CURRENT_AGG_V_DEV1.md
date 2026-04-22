# SUBSCR_FTV_MONTH_CURRENT_AGG_V_DEV1

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a monthly aggregated snapshot of Fast Broadband (BB) and Fast TV (FTV) subscriptions. It correlates individual subscriptions across different product types and source systems (e.g., identifying dual-play customers, particularly for 'LUMINO' services). The view calculates various product and subscription keys for four specific date points (P1, P2, P3, P4, likely representing start/end of previous and current months) relative to the current system date. It also distinguishes between 'Main' (consumer) and 'Businessprodukt' (BED) TV subscriptions and applies product prioritization logic.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[KAS.KUNDE]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[KAS.ABONNENTNR_MSISDN]]
- ← [[CCDW.SUBSCRIBED_PRODUCT_FTV_EXT]]


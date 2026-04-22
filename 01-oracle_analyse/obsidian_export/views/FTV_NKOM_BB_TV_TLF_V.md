# FTV_NKOM_BB_TV_TLF_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and categorizes customer subscriptions for Broadband (BB), TV, and Telephony (TLF) services across multiple historical half-year periods. It calculates the number of active BB, TV, and TLF subscriptions, identifies various product combinations (e.g., 'BB/TV/TLF', 'BB/TV', 'BB/TLF', 'BB', 'TLF') at the customer or address level, and enriches this data with detailed product attributes such as product names, speed, technology, value chain, and dwelling unit type. The view aims to provide a comprehensive overview of multi-play service penetration and composition for reporting and analysis.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[GALAXY.SUBSCR_FTV_MONTH_AGG_V]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]


# V_SUBSCR_FB_MEMBERS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, dated, and product-enriched perspective on subscription members, likely within a telecommunications or service provider domain. It combines core subscription details (identified by 'SUBSCR_FB_MEMBERS') with product metadata (name, family) and temporal information. The view exposes various identifiers (subscription, offer, agreement), dates, and flags related to different services like mobile, fixed broadband, fixed telephony, databonus, and business accounts.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCR_FB_MEMBERS_2018_MV_SRG]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.DATE_DIM_MV]]


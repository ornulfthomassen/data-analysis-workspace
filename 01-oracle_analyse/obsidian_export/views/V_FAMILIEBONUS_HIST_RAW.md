# V_FAMILIEBONUS_HIST_RAW

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view retrieves detailed historical information for specific agreement offers (filtered by PRODUCT_OFFER_ID = 956), likely related to a 'Familiebonus' (Family Bonus) program. It calculates a 'Familiebonus Basis' by converting a configured data usage parameter (in bytes) to gigabytes and then dividing by 0.5. Additionally, it identifies and counts the occurrences of various product/service types (Mobile, Business, SWAP, Fixed Telephony, Fixed Broadband) within another agreement configuration parameter. It combines data from agreement management, data warehousing, online reporting, and product dimension systems to provide a comprehensive view of agreement offers, their configurations, associated subscribed orders, and product details.

## Data Sources (Inputs)
- ← [[CM.AGREEMENT_OFFER]]
- ← [[CM.AGREEMENT_OFFER_COMPONENT]]
- ← [[CCDW.AGREEMENT_MAPPING]]
- ← [[CM.AGREEMENT_OFFER_CONFIGURATION]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_PARAM_ORDER]]
- ← [[ONL_REP.SUBSCRIBED_OFFER_ORDER]]
- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
- ← [[GALAXY.PRODUCT_DIM]]


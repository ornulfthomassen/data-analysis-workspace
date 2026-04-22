# ADM_SWAP_FLAGGING

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view aggregates and processes data related to 'SWAP' agreements, primarily focusing on mobile device (IMEI) usage and associated subscription details. It aims to identify and present the main phone number, owner, and user information for each swap agreement, prioritizing the most recent IMEI usage data. It combines agreement details, product configurations, subscription mappings, and IMEI usage history to provide a comprehensive view of swap agreements, including agreement dates, IMEI details, and associated main numbers (original and current usage).

## Data Sources (Inputs)
- ← [[CCDW.AGREEMENT]]
- ← [[CCDW.AGREEMENT_PRODUCT_CONFIG]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[LIVE.EUREKA_IMEI]]


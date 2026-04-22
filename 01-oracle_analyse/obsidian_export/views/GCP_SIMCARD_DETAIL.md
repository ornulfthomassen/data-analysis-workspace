# GCP_SIMCARD_DETAIL

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated, detailed list of active SIM card information associated with customer subscriptions. It categorizes customers as 'ServiceProvider', 'Business' (Virksomhet), 'Private' (Privat), or 'Unknown' (Ukjent), and links them to their subscriptions, related numbers (MSISDN, ICC_ID), and SIM card specifics such as type, status, start date, eSIM type, and service provider. The view filters for currently active subscriptions and SIM cards, excludes certain `SUBSCRIBED_OFFER_ID`s, and aggregates SIM card start dates and record change dates for unique subscription-SIM card combinations.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.CUSTOMER]]
- ← [[CM.REL_NUMBER]]
- ← [[SIMNR.SIMCARD_DETAILS]]


# DUAL_ACCOUNT_RAPPORT_3B

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies active mobile subscriptions that have a 'Connect ID' associated but lack a corresponding linked user account (specifically, 'tnn_mobile_<SUBSCR_ID>') in the `COMOYO.FIM_USER_ACCOUNTS` system. It retrieves detailed subscription information, associated customer data, and phone verification status, highlighting cases where a linked account is expected but not found.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.CUSTOMER]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.FIM_USER_ACCOUNTS]]


# DUAL_ACCOUNT_RAPPORT_0

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view is designed to identify and report discrepancies or mismatches between two sets of subscription/account data, primarily focusing on 'Dual Accounts' related to 'TnN service provisioning' and 'MSISDN relationship with Connect IDs'. It performs a full outer join between data sourced from `COMOYO.FIM_` tables (representing 'TnN mobile' accounts with null MSISDNs) and data from `CM.SUBSCRIPTION`/`CM.SUBSCRIBED_OFFER_CONFIGURATION` (representing subscriptions with a specific 'Connect ID' parameter 2100). The view specifically filters for records that exist in one of these datasets but not the other, effectively highlighting cases where a `SUBSCR_ID` is present in one system's representation but missing or not matching in the other, and provides diagnostic information for the CM side of the mismatches.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER]]
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.USER_SERVICES_PHONES]]
- ← [[COMOYO.USER_SERVICES]]


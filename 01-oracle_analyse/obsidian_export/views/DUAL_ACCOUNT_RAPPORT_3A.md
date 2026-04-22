# DUAL_ACCOUNT_RAPPORT_3A

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies 'dual accounts' by listing subscriptions that have an associated 'Connect ID' but where this 'Connect ID' does not correspond to an existing user account in the Comoyo FIM (Financial Information Management) system. It also attempts to reconcile the subscription's MSISDN with user phone data from the FIM system and checks if the 'Connect ID' from the subscription matches a 'USER_ID' found in FIM user phone records.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.CUSTOMER]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.FIM_USER_ACCOUNTS]]


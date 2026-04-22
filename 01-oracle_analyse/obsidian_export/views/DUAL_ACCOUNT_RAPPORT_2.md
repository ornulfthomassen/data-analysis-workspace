# DUAL_ACCOUNT_RAPPORT_2

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies 'dual accounts' by listing subscriptions where an MSISDN has a 'CONNECT_ID_SUBS' (likely for service provisioning) but this MSISDN, when prefixed with '47', does not exist as a phone number in the 'FIM_USER_PHONES' table. Essentially, it flags MSISDNs that are active in the subscription management system but are not registered as phones in another specified system, potentially highlighting data inconsistencies or unmanaged devices.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.CUSTOMER]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER_PHONES]]


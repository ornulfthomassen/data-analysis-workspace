# DUAL_ACCOUNT_RAPPORT_1

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies 'Dual Accounts' by comparing Connect IDs. Specifically, it finds instances where a subscriber's Connect ID (from the subscription system 'TnN') is different from the Connect ID associated with the same MSISDN (mobile number) in another system ('TD' or 'Comoyo'). It also compares the subscription's Connect ID with the user ID linked to the account itself. The view flags these discrepancies ('Ulik' for different, 'Lik' for same) for both phone and account-level comparisons.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.CUSTOMER]]
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.FIM_USER_ACCOUNTS]]


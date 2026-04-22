# DUAL_ACCOUNT_RAPPORT_4

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies 'hardlink' user accounts (specifically those where 'ACC_USER_ID' starts with 'tnn_mobile_hardlink') that have an associated 'ACC_MSISDN'. The primary purpose is to find instances where this 'ACC_MSISDN' is *not* registered under the *same* 'USER_ID' in the 'FIM_USER_PHONES' table, but rather is associated with a *different* 'USER_ID' within the phone records. It also retrieves email details and phone verification information related to these accounts and their potentially conflicting MSISDN associations.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
- ← [[COMOYO.FIM_USER_PHONES]]
- ← [[COMOYO.FIM_USER_EMAILS]]


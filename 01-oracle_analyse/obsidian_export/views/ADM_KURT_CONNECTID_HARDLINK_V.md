# ADM_KURT_CONNECTID_HARDLINK_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Consolidates and extracts key identification numbers (KURT_ID, CONNECT_ID, TNUID) and contact details (phone number, email address) for users. It filters for accounts containing a 'HARDLINK_' identifier and specific phone number ranges, prioritizing user data based on the most recent phone verification time.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
- ← [[COMOYO.FIM_USER_EMAILS]]
- ← [[COMOYO.FIM_USER_PHONES]]


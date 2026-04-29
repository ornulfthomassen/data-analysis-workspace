# DUAL_ACCOUNT_RAPPORT_4

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies 'hardlink' user accounts (from COMOYO.FIM_USER_ACCOUNTS) that have an associated MSISDN, where that specific MSISDN is NOT registered under the same USER_ID in COMOYO.FIM_USER_PHONES (indicating a potential mismatch or unregistered phone for that user ID), but might be registered under a different USER_ID in COMOYO.FIM_USER_PHONES. It consolidates account, phone, and email information for these potential 'dual account' scenarios.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |
| ACC_USER_ID |
| ACC_MSISDN |
| ACC_ID |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| PH_MSISDN |
| USER_ID |
| PH_ID |
| PH_VERIFICATION_TIME |
| PH_VERIFIED |
- ← [[COMOYO.FIM_USER_EMAILS]]
| Column Name |
|---|
| USER_ID |
| EMAIL_ADDRESS |
| EMAIL_ID |
| EMAIL_ISPRIMARY |
| EMAIL_VERIFIED |


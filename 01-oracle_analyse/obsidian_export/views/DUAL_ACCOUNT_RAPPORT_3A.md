# DUAL_ACCOUNT_RAPPORT_3A

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies 'dual accounts' by finding subscriptions that have a 'Connect ID' (user identifier) but no corresponding linked account in the FIM_USER_ACCOUNTS table. It essentially reports on subscriptions where the associated Connect ID is orphaned or no longer exists in the central user account management system.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| INFO_CHG_DATE |
| CUST_ID_USER |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| KURT_ID |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_ID |
| VALID_TO_DATE |
| INFO_IS_DELETED |
| PARAMETER_VALUE |
| VALID_FROM_DATE |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| PH_MSISDN |
| USER_ID |
| PH_ID |
| PH_VERIFICATION_TIME |
| PH_VERIFIED |
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |


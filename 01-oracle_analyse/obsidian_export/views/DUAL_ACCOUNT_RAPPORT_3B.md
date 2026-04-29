# DUAL_ACCOUNT_RAPPORT_3B

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies 'dual accounts' by selecting subscription details that have an associated 'Connect ID' but lack a corresponding linked user account in the `COMOYO.FIM_USER_ACCOUNTS` table. It joins subscription, customer, and offer configuration data with `COMOYO.FIM_USER_PHONES` to enrich the results and assess if the user associated with the phone number matches the Connect ID.

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
| ACC_USER_ID |
| USER_ID |


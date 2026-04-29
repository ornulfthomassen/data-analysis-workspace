# DUAL_ACCOUNT_RAPPORT_0B

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and categorizes various 'dual account' or inconsistent relationships between CM subscriptions, MSISDNs, and user IDs across CM, COMOYO FIM, and COMOYO USER_SERVICES systems, focusing on service provisioning and mobile number associations.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_ID |
| VALID_TO_DATE |
| INFO_IS_DELETED |
| VALID_FROM_DATE |
| PARAMETER_VALUE |
- ← [[COMOYO.FIM_USER]]
| Column Name |
|---|
| USER_ID |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| PH_MSISDN |
| USER_ID |
| PH_VERIFIED |
| PH_VERIFICATION_TIME |
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |
| ACC_USER_ID |
- ← [[COMOYO.FIM_USER_EMAILS]]
| Column Name |
|---|
| EMAIL_ADDRESS |
| USER_ID |
| EMAIL_ISPRIMARY |
| EMAIL_VERIFIED |
- ← [[COMOYO.USER_SERVICES_PHONES]]
| Column Name |
|---|
| PHONES |
| USER_ID |
| FILE_DATE |
- ← [[COMOYO.USER_SERVICES]]
| Column Name |
|---|
| FILE_DATE |
| USER_ID |


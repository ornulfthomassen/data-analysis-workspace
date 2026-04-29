# DUAL_ACCOUNT_RAPPORT_0C

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies 'dual accounts' or inconsistencies in phone number verification status across different systems (CM, TD, US) for subscribers. It specifically targets phone numbers associated with a 'Connect ID' (CID) that are either unverified or lack a verification timestamp. It achieves this by linking subscriber data from CM, user information from Comoyo FIM (TD), and user service phone details from Comoyo (US), ensuring the same phone number and Connect ID are present in all linked systems.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| INFO_IS_DELETED |
| SUBSCR_VALID_TO_DATE |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_VALUE |
| PARAMETER_ID |
| VALID_TO_DATE |
| INFO_IS_DELETED |
| VALID_FROM_DATE |
- ← [[COMOYO.FIM_USER]]
| Column Name |
|---|
| USER_ID |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| USER_ID |
| PH_MSISDN |
| PH_VERIFIED |
| PH_VERIFICATION_TIME |
- ← [[COMOYO.USER_SERVICES_PHONES]]
| Column Name |
|---|
| USER_ID |
| FILE_DATE |
| PHONES |


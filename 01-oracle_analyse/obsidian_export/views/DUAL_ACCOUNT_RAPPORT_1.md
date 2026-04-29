# DUAL_ACCOUNT_RAPPORT_1

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies 'dual accounts' by comparing Connect IDs associated with a MSISDN (phone number) across different systems. Specifically, it flags cases where a MSISDN is tied to one Connect ID for service provisioning (from CM system) but is associated with a different Connect ID in the COMOYO system for user phones and accounts. It aims to highlight discrepancies in user-to-phone and user-to-account mappings.

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
| PARAMETER_VALUE |
| VALID_FROM_DATE |
| VALID_TO_DATE |
| INFO_IS_DELETED |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| PH_MSISDN |
| USER_ID |
| PH_ID |
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| ACC_USER_ID |
| USER_ID |


# DUAL_ACCOUNT_RAPPORT_0

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and reports on dual or unlinked accounts by comparing TnN service provisioning data (from FIM_USER and FIM_USER_ACCOUNTS) with CM subscription and MSISDN information (from CM.SUBSCRIPTION and related tables). The view focuses on discrepancies where a subscription ID exists in one system/subquery but not the other, providing details from both sources where available, along with an 'INFO' column describing the status of CM MSISDN/User ID linkage.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER]]
| Column Name |
|---|
| USER_ID |
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |
| ACC_MSISDN |
| ACC_USER_ID |
| ACC_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_FROM_DATE |
| INFO_IS_DELETED |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_ID |
| INFO_IS_DELETED |
| VALID_TO_DATE |
| VALID_FROM_DATE |
| PARAMETER_VALUE |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| PH_MSISDN |
| USER_ID |
- ← [[COMOYO.USER_SERVICES_PHONES]]
| Column Name |
|---|
| USER_ID |
| file_date |
| PHONES |
- ← [[COMOYO.USER_SERVICES]]
| Column Name |
|---|
| USER_ID |
| file_date |


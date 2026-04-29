# DUAL_ACCOUNT_RAPPORT_2

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies subscriptions (MSISDNs) that have a 'Connect ID' configured through a specific subscribed offer configuration (PARAMETER_ID = 2100) but are not found as active phones in the COMOYO.FIM_USER_PHONES system. The view aims to list 'dual accounts' where a service provisioning ID exists for an MSISDN, but the MSISDN itself is not linked as an active phone.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| DIRECTORY_NUMBER_ID |
| CUST_ID_USER |
| SUBSCR_VALID_FROM_DATE |
| INFO_CHG_DATE |
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
| VALID_TO_DATE |
| INFO_IS_DELETED |
| VALID_FROM_DATE |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| PH_MSISDN |


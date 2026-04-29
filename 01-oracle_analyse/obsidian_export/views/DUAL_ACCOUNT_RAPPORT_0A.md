# DUAL_ACCOUNT_RAPPORT_0A

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Identifies and categorizes 'dual account' scenarios in Telenor's service provisioning system where FIM user accounts lack an MSISDN, by correlating FIM account details (from COMOYO schema) with subscription and Connect ID statuses (from CM schema). It distinguishes between closed and open subscriptions and highlights cases requiring manual handling due to potential inconsistencies in Connect ID assignments.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER]]
| Column Name |
|---|
| USER_ID |
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |
| ACC_USER_ID |
| ACC_MSISDN |
| ACC_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCR_ID |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |
- ← [[CM.SUBSCRIBED_OFFER_CONFIGURATION]]
| Column Name |
|---|
| SUBSCR_ID |
| PARAMETER_ID |
| PARAMETER_VALUE |
| INFO_IS_DELETED |
| VALID_TO_DATE |


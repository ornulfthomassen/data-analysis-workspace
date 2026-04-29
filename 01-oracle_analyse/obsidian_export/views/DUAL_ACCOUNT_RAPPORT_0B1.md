# DUAL_ACCOUNT_RAPPORT_0B1

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and reports on 'dual account' scenarios by analyzing the relationship between mobile subscriptions, their associated Connect IDs (CM_USER_ID), and the existence of these Connect IDs in the FIM_USER system. It specifically categorizes discrepancies for both closed and active subscriptions, providing details on MSISDNs, subscription validity, and Connect ID status. The report focuses on 'TnN service provisioning and MSISDN relationship with Connect IDs'.

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
| PARAMETER_VALUE |
| VALID_TO_DATE |
| INFO_IS_DELETED |
| VALID_FROM_DATE |
- ← [[COMOYO.FIM_USER]]
| Column Name |
|---|
| USER_ID |


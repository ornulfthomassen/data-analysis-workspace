# P_ADR_ODS_MSISDN_SERVICE_PROVIDER

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure generates a comprehensive, de-duplicated list of active and recently inactive mobile subscriptions (MSISDNs) for Telenor, Talkmore, and Dipper customers. It determines the service provider, Telenor division (consumer/business), and subscription status. The data is stored in the CLM_CCM.ODS_MSISDN_SERVICE_PROVIDER table using a full-load 'table swap' methodology, where new data is built into a temporary table, then swapped with the existing main table, which is retained as a backup. It also includes error handling and logging of the process status.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_MSISDN_SERVICE_PROVIDER]]
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| DIRECTORY_NUMBER_ID |
| SUBSCR_VALID_TO_DATE |
| S212_REF_ID_RESP |
| SUBSCR_HAS_SECRET_NUMBER |
| SUBSCR_STATUS_ID |
| SUBSCR_VALID_FROM_DATE |
| CUST_ID_USER |
| INFO_IS_DELETED |
| SYSTEM_TYPE_ID |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| CUST_LAST_NAME |
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |

## Target Tables (Outputs)
- → [[CLM_CCM.ODS_MSISDN_SERVICE_PROVIDER_N]]
| Column Name |
|---|
| MAIN_NUMBER |
| CURRENT_STATUS |
| SERVICE_TYPE |
| SERVICE_PROVIDER |
| TELENOR_DIVISION |
| SUBSCR_HAS_SECRET_NUMBER |
| SUBSCR_STATUS_ID |
| R_NUM |
- → [[CLM_CCM.ODS_MSISDN_SERVICE_PROVIDER]]
| Column Name |
|---|
| MAIN_NUMBER |
| CURRENT_STATUS |
| SERVICE_TYPE |
| SERVICE_PROVIDER |
| TELENOR_DIVISION |
| SUBSCR_HAS_SECRET_NUMBER |
| SUBSCR_STATUS_ID |
| R_NUM |
- → [[CLM_CCM.ODS_MSISDN_SERVICE_PROVIDER_O]]
| Column Name |
|---|
| MAIN_NUMBER |
| CURRENT_STATUS |
| SERVICE_TYPE |
| SERVICE_PROVIDER |
| TELENOR_DIVISION |
| SUBSCR_HAS_SECRET_NUMBER |
| SUBSCR_STATUS_ID |
| R_NUM |
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| STATUS |
| MESSAGE |
| WF_NAME |
| S_NAME |


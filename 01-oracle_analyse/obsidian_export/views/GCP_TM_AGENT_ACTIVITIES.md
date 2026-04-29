# GCP_TM_AGENT_ACTIVITIES

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a unified view of Telemarketing (TM) agent activity data, including contact events, customer information, agent details, and call metrics, primarily for reporting purposes in SAS Viya.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.DIM_AGENTS]]
| Column Name |
|---|
| FULL_NAME |
| EMAIL_ADDRESS |
| DELETE_DATE |
| CREATE_DATE |
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
| Column Name |
|---|
| ID |
| ACCOUNT_NUMBER |
| WORKGROUP_NAME |
| TIME_OF_CONTACT |
| LIST_TEMPLATE_NAME |
| DIALER_TARGET_NAME |
| RESPONSE_STATUS |
| RECORD_RELEASED_TIME |
| OV_TRUNK_RELEASED_TIME |
| OV_CALL_CONNECTED_TIME |
| OV_CALL_ANSWERED_TIME |
| OV_DIAL_COMPLETE_TIME |
| OV_DIAL_START_TIME |
| UMID |
| CALL_TYPE |
| AGENT_EMAIL |
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
| Column Name |
|---|
| ACCOUNTNR |
| CAMPAIGN_CD |
| COMMUNICATION_CD |
| OCCURENCE_ID |
| CELL_PACKAGE_SK |
| RESP_TRACKING_CD |
| KURT_ID |
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
| Column Name |
|---|
| DISPOSITION_TYPE_DESC |
| DISPOSITION_DESC |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |


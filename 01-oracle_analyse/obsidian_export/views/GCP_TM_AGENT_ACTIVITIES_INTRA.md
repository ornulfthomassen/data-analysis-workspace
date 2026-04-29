# GCP_TM_AGENT_ACTIVITIES_INTRA

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a unified view of TM (Telemarketing) agent activity data for reporting in Google Cloud Platform, combining contact events, customer account details, agent information, and disposition descriptions.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.CL_CONTACT_EVENT_INTRA]]
| Column Name |
|---|
| ID |
| ACCOUNT_NUMBER |
| WORKGROUP_NAME |
| TIME_OF_CONTACT |
| LIST_TEMPLATE_NAME |
| CONTACT_LIST_NAME |
| DIALER_TARGET_NAME |
| RESPONSE_STATUS |
| RECORD_RELEASED_TIME |
| OV_TRUNK_RELEASED_TIME |
| OV_CALL_CONNECTED_TIME |
| OV_CALL_ANSWERED_TIME |
| OV_DIAL_COMPLETE_TIME |
| OV_DIAL_START_TIME |
| UMID |
| AGENT_EMAIL |
| CALL_TYPE |
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
| Column Name |
|---|
| CAMPAIGN_CD |
| COMMUNICATION_CD |
| OCCURENCE_ID |
| CELL_PACKAGE_SK |
| RESP_TRACKING_CD |
| ACCOUNTNR |
| KURT_ID |
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
| Column Name |
|---|
| DISPOSITION_DESC |
| DISPOSITION_TYPE_DESC |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |
- ← [[TM_DIALER_C.DIM_AGENTS]]
| Column Name |
|---|
| FULL_NAME |
| EMAIL_ADDRESS |
| DELETE_DATE |
| CREATE_DATE |


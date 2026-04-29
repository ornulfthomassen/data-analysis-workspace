# TST_TM_AGENT_ACTIVITIES_INTRA

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates agent activity data from a dialer system by joining contact events with agent details, customer account information, disposition descriptions, and SAS marketing campaign metadata, providing a detailed view of customer interactions.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.DIM_AGENTS]]
| Column Name |
|---|
| FULL_NAME |
| EMAIL_ADDRESS |
| DELETE_DATE |
| CREATE_DATE |
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
| ACCOUNTNR |
| CAMPAIGN_CD |
| COMMUNICATION_CD |
| OCCURENCE_ID |
| CELL_PACKAGE_SK |
| RESP_TRACKING_CD |
| RESPONSE_TRACKING_CD |
| SRC_ID |
| SEGMENT_MAP_CODE |
| TASK_CODE |
| TASK_OCCURRENCE_NUMBER |
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
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
| Column Name |
|---|
| TASK_CD |
| ACTIVITYDESC |
| CAMPAIGNDESC |
| CREATED_DTTM |


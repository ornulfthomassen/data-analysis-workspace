# TST_TM_AGENT_ACTIVITIES

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches agent activity data from various dialer and customer relationship management (CRM) sources. It captures details about contact events, customer interactions, agent information, call metrics (including calculated durations), and campaign details. The primary purpose is to prepare and transform this 'Dialer-info' for further analytical processing or loading into a data warehouse (referred to as Mjøsa in the comments). It also standardizes agent identifiers and categorizes activities by dealer ID based on workgroup names.

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
| CONTACT_LIST_NAME |
| DIALER_TARGET_NAME |
| RESPONSE_STATUS |
| AGENT_EMAIL |
| RECORD_RELEASED_TIME |
| OV_TRUNK_RELEASED_TIME |
| OV_CALL_CONNECTED_TIME |
| OV_CALL_ANSWERED_TIME |
| OV_DIAL_COMPLETE_TIME |
| OV_DIAL_START_TIME |
| UMID |
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


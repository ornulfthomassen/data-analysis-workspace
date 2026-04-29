# VYA_TM_AGENT_ACTIVITIES

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates agent activity data from a dialer system (Alvaria Via) with customer mapping, campaign details, and agent information. It provides a comprehensive record of outbound contact events, including activity identifiers, customer and campaign metadata, agent login details, contact timestamps, call durations, and disposition status. The purpose is to load dialer-related information into a data warehouse or analytical system (Mjøsa).

## Data Sources (Inputs)
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
| CAMPAIGN_CD |
| COMMUNICATION_CD |
| OCCURENCE_ID |
| CELL_PACKAGE_SK |
| RESP_TRACKING_CD |
| ACCOUNTNR |
| KURT_ID |
- ← [[TM_DIALER_C.DIM_AGENTS]]
| Column Name |
|---|
| FULL_NAME |
| EMAIL_ADDRESS |
| DELETE_DATE |
| CREATE_DATE |
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


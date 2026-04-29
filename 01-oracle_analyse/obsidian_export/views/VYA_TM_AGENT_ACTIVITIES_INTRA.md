# VYA_TM_AGENT_ACTIVITIES_INTRA

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a consolidated record of agent activities and customer contact events, primarily sourced from the Dialer system (Alvaria Via). It combines details about agent interactions, customer account information, campaign data, and disposition statuses. It also calculates contact and call durations and links to a customer mapping for a unified customer key. The `INTRA` suffix likely indicates it focuses on internal or intra-day activity tracking.

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


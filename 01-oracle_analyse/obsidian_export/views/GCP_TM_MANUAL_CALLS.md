# GCP_TM_MANUAL_CALLS

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates detailed information about manual telephone calls, including call duration, agent, and call list specifics. It enriches this call data by linking it to customer information (KURT_ID/CUSTOMER_SK) from various internal sources, providing insights into customer relations, reservation statuses (internal and external), and the origin of customer contact details, primarily used for data loading to Mjøsa.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
| Column Name |
|---|
| KURT_KEY |
| CUSTOMER_KEY |
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
| Column Name |
|---|
| KURT_ID |
| CU_NO_MPP |
| CU_NO_MPP_USR |
| CU_NO_MPR |
| CU_NO_MPR_USR |
| CU_NO_MBB |
| CU_NO_MBB_USR |
| CU_NO_FWA |
| CU_NO_FWA_USR |
| CU_NO_FBR |
| CU_NO_FBR_USR |
| CU_NO_FBR_TNN |
| CU_NO_FBR_TNN_USR |
| CU_NO_FBB_FBR_FTV |
| CU_NO_FBB_FBR_FTV_USR |
| CU_NO_FIX_BBT_FTV |
| CU_NO_FIX_BBT_TNN |
| CU_NO_FBB_COAX |
| CU_NO_FBB_COAX_USR |
- ← [[ODS.CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| CUSTOMER_ID |
| TM_IND_BR |
| BR_TM_MAX_RES_APP_DTTM |
| TM_IND_INTERNAL |
| TM_MAX_RES_APP_DTTM |
| SMS_NUMBER |
| SMS_AL_MAX_DTTM |
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
| Column Name |
|---|
| ACCOUNTNR |
| KURT_ID |
| INSERT_DTTM |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| KURT_ID_USER |
| MAIN_NUMBER |
| BUSINESS_AREA_ID |
| CURRENT_STATUS |
- ← [[REFERENCE.CONSUMER_CUST_INFO]]
| Column Name |
|---|
| NUMBER1 |
| CONTACTPHONENUMBER1 |
| TEXT2 |
| DATAREGDATE |
| TEXT1 |
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
| Column Name |
|---|
| SEQNUM |
| ACCOUNT_NUMBER |
| TIME_OF_CONTACT |
| RESPONSE_STATUS |
| AGENT_EMAIL |
| AGENT_FULL_NAME |
| OV_TRUNK_RELEASED_TIME |
| OV_CALL_CONNECTED_TIME |
| OV_PHONE_NUMBER |
| WORKGROUP_NAME |
| CONTACT_LIST_NAME |
| DIALER_TARGET_NAME |
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
| Column Name |
|---|
| DISPOSITION_DESC |
| DISPOSITION_TYPE_DESC |
- ← [[TM_DIALER_C.AGENTLOGINLOGOUT]]
| Column Name |
|---|
| USER_ID |
| LOGINDT |
| WORKGROUP_ID |
- ← [[TM_DIALER_C.WORKGROUPDVAUDIT]]
| Column Name |
|---|
| WORKGROUP_ID |
| WORKGROUP_NAME |
- ← [[TM_DIALER_C.MANUALCALLDETAIL]]
| Column Name |
|---|
| SEQNUM |
| DNIS |
| CALLSTARTDT |
| CALLENDDT |
| CONNECTDT |
| CONNCLEARDT |
| USER_ID |
| WORKGROUP_ID |
| SERVICE_ID |
- ← [[TM_DIALER_C.SERVICEDVAUDIT]]
| Column Name |
|---|
| SERVICE_ID |
| SERVICE_C |
- ← [[TM_DIALER_C.USERSDVAUDIT]]
| Column Name |
|---|
| USER_ID |
| USER_F_NAME |
| USER_L_NAME |
| EMAILADDRESS |


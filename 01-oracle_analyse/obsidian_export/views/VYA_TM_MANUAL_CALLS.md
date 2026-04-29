# VYA_TM_MANUAL_CALLS

**Schema:** `CCM` | **Type:** `View`

## Description
This view compiles a detailed record of manual outbound calls by integrating call details with customer information from various sources (account lists, subscriptions, reference data, reservation data). It links calls to customer IDs, determines the source of the customer ID, calculates call duration, and enriches the data with customer reservation statuses (brand registry and internal) and subscription counts to provide a comprehensive view of telemarketing interactions and customer relationships. The output includes call specific details, agent information, customer identifiers, and various reservation/relationship indicators.

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
| DIALER_TARGET_NAME |
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
| Column Name |
|---|
| DISPOSITION_TYPE_DESC |
| DISPOSITION_DESC |
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
- ← [[TM_DIALER_C.MANUALCALLDETAIL]]
| Column Name |
|---|
| SEQNUM |
| DNIS |
| CALLSTARTDT |
| CALLENDDT |
| CONNECTDT |
| CONNCLEARDT |
| SERVICE_ID |
| WORKGROUP_ID |
| USER_ID |


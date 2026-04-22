# GCP_TM_MANUAL_CALLS

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'GCP_TM_MANUAL_CALLS', provides a comprehensive and consolidated dataset of manual calls made through a TM Dialer system. Its primary function is to link detailed call event data (duration, agent, work type) with extensive customer information, including customer keys (KURT_ID, CUSTOMER_SK), account details, subscription relations, and reservation statuses (e.g., 'Do Not Call' lists). It identifies the called customer through multiple lookup mechanisms (calling list, phone number in various customer databases) and enriches the call records with customer relation flags and reservation indicators, potentially for compliance, reporting, or further data warehousing for analysis of telemarketing activities.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
- ← [[ODS.CUSTOMER_RES_AND_APP]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[REFERENCE.CONSUMER_CUST_INFO]]
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[TM_DIALER_C.AGENTLOGINLOGOUT]]
- ← [[TM_DIALER_C.WORKGROUPDVAUDIT]]
- ← [[TM_DIALER_C.MANUALCALLDETAIL]]
- ← [[TM_DIALER_C.SERVICEDVAUDIT]]
- ← [[TM_DIALER_C.USERSDVAUDIT]]


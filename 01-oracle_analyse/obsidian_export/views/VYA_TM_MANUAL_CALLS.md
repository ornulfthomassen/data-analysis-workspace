# VYA_TM_MANUAL_CALLS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive record of manual outbound calls made by agents, enriching each call entry with detailed customer information. It identifies the customer associated with the called phone number by attempting to match it against various data sources (account lists, subscription data, consumer information, and reservation applications). The view then includes customer subscription status and reservation flags (e.g., 'BR' and 'Internal' reservations) for different campaigns, along with call metadata such as duration, agent ID, and work type. Its purpose is to consolidate call details with customer profiles and reservation statuses, likely for analysis related to customer interaction strategies or campaign effectiveness, as hinted by the 'Loading MIN SKY-usage to Mjøsa' comment.

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


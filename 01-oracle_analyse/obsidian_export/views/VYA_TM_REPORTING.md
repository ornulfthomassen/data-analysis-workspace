# VYA_TM_REPORTING

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_TM_REPORTING, is designed to consolidate and prepare detailed Telephony Management (TM) and customer contact event data for reporting purposes, specifically for SAS Viya. It combines information about customer accounts, campaign details, communication strategies, and various contact events (outbound calls, SMS, inbound calls, manual calls). The view calculates and derives numerous metrics and indicators related to call duration, wrap-up time, contact channels, response statuses (e.g., success, failure, delivered, not delivered), agent activities, and record expiry. It enriches the core contact data with details on agent IDs, disposition names, and updated expiry information.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.USERSDVAUDIT]]
- ← [[TM_DIALER_C.CQ_DISPOSITION]]
- ← [[CLM_CCM.CCM_TM_ACNT_LIST_UPD_V]]
- ← [[TM_DIALER_C.ACDCALLDETAIL]]
- ← [[TM_DIALER_C.SERVICEDVAUDIT]]
- ← [[TM_DIALER_C.MANUALCALLDETAIL]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]


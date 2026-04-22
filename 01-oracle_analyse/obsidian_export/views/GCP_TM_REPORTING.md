# GCP_TM_REPORTING

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named GCP_TM_REPORTING, is designed to provide comprehensive Telemarketing (TM) data for reporting purposes, particularly for Google Cloud Platform (GCP) Looker. It consolidates information from various call center and customer management systems to offer a detailed overview of customer interactions, campaign performance, agent activities, call outcomes (e.g., attempts, contacts, SMS status), and call durations. It tracks historical data up to 365 days prior and includes derived indicators for expired records, different types of attempts (voice, SMS), callbacks, and call types (inbound/manual).

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


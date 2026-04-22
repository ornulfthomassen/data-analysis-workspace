# GCP_TM_AGENT_ACTIVITIES_INTRA

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and prepares agent activity data from a dialer system (Alvaria Via) for reporting in Google Cloud Platform (GCP Looker). It combines contact event details with customer information, campaign data, agent details, and call disposition descriptions. The view specifically filters for voice calls, calculates various call and contact card durations, and derives an activity dealer ID.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.DIM_AGENTS]]
- ← [[TM_DIALER_C.CL_CONTACT_EVENT_INTRA]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


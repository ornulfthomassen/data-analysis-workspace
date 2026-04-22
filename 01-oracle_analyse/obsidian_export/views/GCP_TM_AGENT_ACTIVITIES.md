# GCP_TM_AGENT_ACTIVITIES

**Schema:** `CCM` | **Type:** `View`

## Description
This view, GCP_TM_AGENT_ACTIVITIES, is designed to consolidate and process agent-customer interaction data (specifically voice calls) for reporting and analytics, primarily used by SAS Viya. It combines detailed contact event information, agent details, customer mapping, and disposition statuses. The view calculates various durations (customer contact card duration, call duration), derives agent IDs, and categorizes activities by dealer based on workgroup names. It filters for voice calls, excludes specific agent emails, and includes activities from April 6, 2021, onwards.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[TM_DIALER_C.DIM_AGENTS]]


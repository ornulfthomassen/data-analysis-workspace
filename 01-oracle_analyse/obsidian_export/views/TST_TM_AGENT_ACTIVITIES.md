# TST_TM_AGENT_ACTIVITIES

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'TST_TM_AGENT_ACTIVITIES', is designed to consolidate and prepare detailed information about agent-led customer interactions, specifically voice calls (dialer activities). It enriches raw contact event data with agent details, campaign information, customer identifiers, and call metrics (like duration and response status) for loading into a data warehouse or reporting system (referred to as 'Mjøsa'). The view calculates various call duration metrics and maps workgroup names to dealer IDs, providing a comprehensive overview of agent activity.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.DIM_AGENTS]]
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


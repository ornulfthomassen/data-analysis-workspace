# VYA_TM_AGENT_ACTIVITIES

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'VYA_TM_AGENT_ACTIVITIES', is designed to extract and transform detailed agent activity and customer contact data from the 'TM_DIALER_C' schema (likely an 'Alvaria Via' dialer system) for loading into a data warehouse or analytical system ('Mjøsa'). It combines information about customer contact events, agent details, campaign attributes, customer mappings, and disposition statuses. The view calculates various call and contact durations, standardizes activity order IDs, and maps workgroup names to dealer IDs. It specifically filters for voice calls, valid agent emails, and recent contact data, preparing a comprehensive dataset for analytical purposes, including integration with SAS Marketing Automation and Customer Intelligence 360.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.CL_CONTACT_EVENT]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.DIM_AGENTS]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


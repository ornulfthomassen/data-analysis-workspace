# TST_TM_AGENT_ACTIVITIES_INTRA

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to consolidate and enrich customer contact activity data from a dialer system (Alvaria Via) for loading into a data warehouse ('Mjøsa'). It combines information about contact events, customer accounts, agent details, call dispositions, and campaign/communication metadata. The view calculates various call duration metrics and associates activities with customer and campaign identifiers. It primarily focuses on voice calls, filters out internal agent activities, and limits data to the last 60 days.

## Data Sources (Inputs)
- ← [[TM_DIALER_C.DIM_AGENTS]]
- ← [[TM_DIALER_C.CL_CONTACT_EVENT_INTRA]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]


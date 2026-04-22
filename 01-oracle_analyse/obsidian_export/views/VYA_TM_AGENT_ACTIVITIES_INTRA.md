# VYA_TM_AGENT_ACTIVITIES_INTRA

**Schema:** `CCM` | **Type:** `View`

## Description
This view compiles and processes agent call activity data for the current day from a dialer system. It enriches the activity records with agent, customer, campaign, and disposition details, calculates various call and contact durations, and maps workgroup names to dealer IDs. The primary purpose is to prepare this consolidated and transformed data for loading into a data warehouse (referred to as Mjøsa). It specifically filters for voice calls (`CALL_TYPE = 'V'`) and recent activities (`TIME_OF_CONTACT >= trunc(sysdate)`).

## Data Sources (Inputs)
- ← [[TM_DIALER_C.DIM_AGENTS]]
- ← [[TM_DIALER_C.CL_CONTACT_EVENT_INTRA]]
- ← [[TM_DIALER_C.A_VIA_CUST_ACCOUNT_LIST]]
- ← [[TM_DIALER_C.DIM_DISPOSITIONS]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]


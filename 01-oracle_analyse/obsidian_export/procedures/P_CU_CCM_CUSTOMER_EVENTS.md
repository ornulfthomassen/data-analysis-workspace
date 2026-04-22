# P_CU_CCM_CUSTOMER_EVENTS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_CU_CCM_CUSTOMER_EVENTS` is designed to generate and refresh customer event data by combining two main types of events: 'Beautiful Exit' and 'Winback'. It extracts data related to mobile number portability, customer subscriptions, product information, and customer demographics. The processed data is staged in temporary work tables, consolidated into a new target table, and then swapped with the existing `CLM_CCM.CCM_CUSTOMER_EVENTS` table to provide an updated dataset. This update mechanism ensures high availability and creates a backup of the previous data. The generated event data is intended for use in customer engagement platforms like SAS CI 360.

## Data Sources (Inputs)
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CLM_CCM.CCM_CUST_CONTACT_PHONE_V]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

## Target Tables (Outputs)
- → [[WORK_BEAUTIFUL_EXIT]]
- → [[WORK_WINBACK_14D]]
- → [[CCM_CUSTOMER_EVENTS_N]]
- → [[CCM_CUSTOMER_EVENTS]]
- → [[CCM_CUSTOMER_EVENTS_O]]


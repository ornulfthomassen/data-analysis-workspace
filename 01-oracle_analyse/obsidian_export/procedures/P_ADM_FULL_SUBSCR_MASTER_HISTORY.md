# P_ADM_FULL_SUBSCR_MASTER_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The `P_ADM_FULL_SUBSCR_MASTER_HISTORY` procedure is designed to build and maintain a comprehensive historical master table (`ADM_SUBSCRIPTION_MASTER_HIST`) for telecommunication subscriptions. It processes subscription data to track changes in main numbers, parent subscriptions, owner/payer/user details, market areas, product keys, and porting events (both inbound and outbound for mobile and fixed lines). The procedure uses a multi-step approach involving the creation and population of several temporary staging tables to aggregate and transform raw data. It then incrementally updates and inserts processed data into various permanent core tables and the final master history table. Backup tables are created before modifying the main persistent tables.

## Data Sources (Inputs)
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_ADM.ADM_MOB_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.ADM_MOB_SUBSCR_OUT_PORT]]
- ← [[CLM_ADM.ADM_FIX_TLF_PORT_IN]]
- ← [[CLM_ADM.ADM_FIX_TLF_PORT_OUT]]
- ← [[CLM_ADM.ADM_FULL_SUBSCR_CORE]]
- ← [[CLM_ADM.TMP_MOB_CORE]]
- ← [[CLM_ADM.TMP_MOB_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.TMP_MOB_SUBSCR_OUT_PORT]]
- ← [[CLM_ADM.TMP_FIX_TLF_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.TMP_FIX_TLF_SUBSCR_OUT_PORT]]
- ← [[CLM_ADM.TMP_FIX_TLF_SUBSCRIPTION_CORE]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_FIX_TLF_SUBSCRIPTION_CORE]]
- → [[CLM_ADM.TMP_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.BDM_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.ADM_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.TMP_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.BDM_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.TMP_FIX_TLF_SUBSCR_IN_PORT]]
- → [[CLM_ADM.BDM_FIX_TLF_SUBSCR_IN_PORT]]
- → [[CLM_ADM.ADM_FIX_TLF_SUBSCR_IN_PORT]]
- → [[CLM_ADM.TMP_FIX_TLF_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.BDM_FIX_TLF_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_FIX_TLF_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- → [[CLM_ADM.BDM_FULL_SUBSCR_CORE]]
- → [[CLM_ADM.ADM_FULL_SUBSCR_CORE]]
- → [[CLM_ADM.TMP_MOB_CORE]]
- → [[CLM_ADM.TMP_FIX_TLF_SUBSCRIPTION_CORE]]


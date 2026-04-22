# P_ADM_FULL_MOB_SUBSCR_MASTER_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (P_ADM_FULL_MOB_SUBSCR_MASTER_HISTORY) is designed to build and maintain a comprehensive historical master table for mobile subscriptions within the CLM_ADM schema. It achieves this by extracting raw subscription data, processing it through multiple intermediate stages to derive historical attributes (like previous subscriptions, owners, payers, market areas), and integrating mobile port-in and port-out information. The procedure uses a series of temporary and permanent staging tables to incrementally build and refine the data before consolidating it into a final ADM_FULL_SUBSCR_MASTER_HISTORY table. It includes mechanisms for data cleansing, creating backups of permanent tables for recovery, gathering statistics, and logging execution details.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[CRM_ANALYSE.PD]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[CLM_ADM.ADM_MOB_FULL_SUBSCR_RAW]]
- ← [[CLM_ADM.TMP_FULL_MOB_SUBSCR_CORE]]
- ← [[CLM_ADM.ADM_FULL_MOB_SUBSCR_CORE]]
- ← [[CLM_ADM.TMP_FULL_MOB_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.ADM_FULL_MOB_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.TMP_FULL_MOB_SUBSCR_OUT_PORT]]
- ← [[CLM_ADM.ADM_FULL_MOB_SUBSCR_OUT_PORT]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MOB_FULL_SUBSCR_RAW]]
- → [[CLM_ADM.TMP_FULL_MOB_SUBSCR_CORE]]
- → [[CLM_ADM.B_TMP_FULL_MOB_SUBSCR_CORE]]
- → [[CLM_ADM.ADM_FULL_MOB_SUBSCR_CORE]]
- → [[CLM_ADM.BDM_FULL_MOB_SUBSCR_CORE]]
- → [[CLM_ADM.TMP_FULL_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.ADM_FULL_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.BDM_FULL_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.TMP_FULL_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_FULL_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.BDM_FULL_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_FULL_SUBSCR_MASTER_HISTORY]]


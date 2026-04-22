# P_ADM_SUBSCR_MASTER_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_ADM_SUBSCR_MASTER_HIST` is designed to build and maintain comprehensive historical master tables for both mobile and fixed-line subscriptions. It processes raw subscription data, derives historical relationships (e.g., previous/original subscriptions, changes in ownership/users), and enriches the data with dealer and product information. It also integrates mobile port-in and port-out events, accumulating new records into dedicated tables. The procedure creates several intermediate 'RAW' tables and temporary tables for calculations, culminating in a detailed mobile subscription history table (`ADM_SUBSCRIPTION_MASTER_HIST`). Additionally, it includes logic for correcting `PARENT_SUBSCRIPTION_ID` in an intermediate raw table and identifies/corrects 'duplicate new sales' entries in the final history table.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[NRPORT.NRPORT_PORTERINGER]]
- ← [[GALAXY.DEALER_DIM]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
- ← [[CLM_ADM.ADM_DEALER_START]]
- ← [[CLM_ADM.ADM_MOB_SUBSCR_MASTER_RAW1]]
- ← [[CLM_ADM.ADM_MOB_SUBSCR_MASTER_RAW2]]
- ← [[CLM_ADM.ADM_FIX_SUBSCR_MASTER_RAW1]]
- ← [[CLM_ADM.ADM_MOB_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.ADM_MOB_SUBSCR_OUT_PORT]]
- ← [[CLM_ADM.TMP_MOB_SUBSCR_IN_PORT]]
- ← [[CLM_ADM.TMP_MOB_SUBSCR_OUT_PORT]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MOB_SUBSCR_MASTER_RAW1]]
- → [[CLM_ADM.ADM_MOB_SUBSCR_MASTER_RAW2]]
- → [[CLM_ADM.ADM_FIX_SUBSCR_MASTER_RAW1]]
- → [[CLM_ADM.ADM_FIX_SUBSCR_MASTER_RAW2]]
- → [[CLM_ADM.TMP_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.ADM_MOB_SUBSCR_IN_PORT]]
- → [[CLM_ADM.TMP_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_MOB_SUBSCR_OUT_PORT]]
- → [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
- → [[CLM_ADM.TDM_SUBSCRIPTION_MASTER_HIST]]


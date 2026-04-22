# P_RDM_CUSTOMER_MAPPING_UPDATE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_RDM_CUSTOMER_MAPPING_UPDATE` is designed to maintain and update a central customer mapping table (`CLM_ADM.ADM_CUSTOMER_MAPPING`). It orchestrates a complex process involving backup management, creation of temporary working tables, processing various subscription data sources to identify customer relationships (owners and users), and applying updates and inserts to the main customer mapping table. The procedure uses control tables to manage the execution flow, track processing status, and provide robust error handling and recovery mechanisms. It also creates historical snapshots of the customer mapping data.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_UD]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_PD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_FIX_BB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_FIX_TLF_SUBSCRIPTION_CORE]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[KURT.KURT]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_D<V_NUMBER_DATE>]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BCK_UD]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BCK_UD_OK]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_RAW]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_UD]]


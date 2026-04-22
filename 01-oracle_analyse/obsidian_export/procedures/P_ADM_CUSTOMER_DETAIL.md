# P_ADM_CUSTOMER_DETAIL

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure generates detailed customer information for a given month (`P_YYYYMM`). It aggregates various subscription data (owner and user subscriptions) and external analytical data from sources like 'BRING_ANALYTIC_UNIVERSE_HIST', based on customer core and mapping information. This processed data is initially created in a temporary table (`TMP_CUSTOMER_DETAIL`) and then efficiently loaded into a specific partition of the permanent `ADM_CUSTOMER_DETAIL` table using a partition exchange operation. The procedure also manages the creation of new partitions if they don't exist and ensures the temporary table is dropped before creation and after use.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.ADM_KURT_OWNER_SUBS_AGG]]
- ← [[CRM_ANALYSE.ADM_KURT_USER_SUBS_AGG]]
- ← [[CRM_ANALYSE.BRING_ANALYTIC_UNIVERSE_HIST]]

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_DETAIL]]
- → [[ADM_CUSTOMER_DETAIL]]


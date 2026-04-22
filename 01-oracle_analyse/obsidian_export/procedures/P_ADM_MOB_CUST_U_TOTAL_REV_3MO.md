# P_ADM_MOB_CUST_U_TOTAL_REV_3MO

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure calculates and aggregates mobile customer subscription and revenue data for a specified month (`V_YYYYMM`). It first creates a temporary staging table (`TMP_MOB_CUST_U_TOTAL_REV_3MO`) with the aggregated results derived from various source tables. Subsequently, it integrates this temporary data into a corresponding partition of a permanent, partitioned analytical table (`ADM_MOB_CUST_U_TOTAL_REV_3MO`) using an efficient partition exchange operation. The procedure also handles checks for source data availability, manages partition creation for the target table, and updates load history.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_MOB_CUST_U_TOTAL_REV_3MO]]
- → [[ADM_MOB_CUST_U_TOTAL_REV_3MO]]


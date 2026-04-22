# P_ADM_MOB_CUST_U_TOT_P_REV_3MO

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates mobile customer subscription and revenue data for a specified period (identified by V_YYYYMM, likely representing a month-year, possibly for a 3-month window as per '3MO' in the name). It first creates a temporary table (`TMP_MOB_CUST_U_TOT_P_REV_3MO`) to store these aggregated results. Then, it uses this temporary table to load the data into a specific partition of a permanent, partitioned analytical table (`ADM_MOB_CUST_U_TOT_P_REV_3MO`). The process involves checking for the existence of the target partition, creating it if it doesn't exist, and then performing a partition exchange to efficiently update or insert the data. It also includes error handling, source data validation, and statistics gathering for the updated table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_MOB_CUST_U_TOT_P_REV_3MO]]
- → [[ADM_MOB_CUST_U_TOT_P_REV_3MO]]


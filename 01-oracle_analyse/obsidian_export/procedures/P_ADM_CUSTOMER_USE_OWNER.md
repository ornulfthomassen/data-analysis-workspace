# P_ADM_CUSTOMER_USE_OWNER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure processes and aggregates customer subscription usage data for a specified month (P_YYYYMM). It performs the following steps:
1.  Initializes variables for the temporary table (TMP_CUSTOMER_USE_OWNER), the target partitioned table (ADM_CUSTOMER_USE_OWNER), and the specific partition name.
2.  Checks for and drops any pre-existing temporary table named 'TMP_CUSTOMER_USE_OWNER' to ensure a clean slate.
3.  Checks if the target monthly partition for 'ADM_CUSTOMER_USE_OWNER' already exists. If not, it dynamically adds the new partition to the table.
4.  Dynamically creates a new temporary table ('TMP_CUSTOMER_USE_OWNER') by selecting and aggregating data from 'ADM_CUSTOMER_CORE', 'ADM_CUSTOMER_MAPPING', 'ADM_KURT_OWNER_SUBS_AGG', and 'ADM_KURT_USER_SUBS_AGG' for the specified month.
5.  Performs a partition exchange operation, swapping the content of the newly created temporary table with the corresponding monthly partition in the permanent 'ADM_CUSTOMER_USE_OWNER' table. This is an efficient way to load data into partitioned tables.
6.  Gathers statistics on the updated partition of 'ADM_CUSTOMER_USE_OWNER' to optimize query performance.
7.  Includes error handling to report any failures during execution.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.ADM_KURT_OWNER_SUBS_AGG]]
- ← [[CRM_ANALYSE.ADM_KURT_USER_SUBS_AGG]]

## Target Tables (Outputs)
- → [[TMP_CUSTOMER_USE_OWNER]]
- → [[ADM_CUSTOMER_USE_OWNER]]


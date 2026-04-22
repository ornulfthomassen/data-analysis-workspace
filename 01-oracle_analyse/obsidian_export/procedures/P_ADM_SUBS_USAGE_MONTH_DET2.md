# P_ADM_SUBS_USAGE_MONTH_DET2

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_SUBS_USAGE_MONTH_DET2`, processes and aggregates detailed mobile subscription usage data for a specified month (`P_YYYYMM`). It performs a series of steps:
1.  **Source Data Validation**: It first checks the availability and integrity of source data in `GALAXY.DATE_DIM_MV` and `GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V` for the target month.
2.  **Temporary Table Management**: It uses a temporary staging table, `TMP_SUBS_USAGE_MONTH_DET`, which is dropped if it exists from a previous run, to hold the aggregated data.
3.  **Partition Management**: For the permanent target table, `ADM_SUBS_USAGE_MONTH_DET2`, it checks if the monthly partition already exists. If not, it creates a new partition for the target month. It includes logic to prevent overwriting existing data in a partition unless explicitly allowed.
4.  **Data Transformation and Aggregation**: It constructs the aggregated usage data by joining various source tables (`CLM_ADM.ADM_MONTH_DIM`, `GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V`, `CCDW.SUBSCRIPTION_MAPPING`, `CM.REL_SUBSCRIPTION`). The aggregation involves summing various usage metrics (e.g., call price, net/gross amounts, volume, duration, roaming cost) and grouping by numerous dimensional keys (e.g., subscription ID, product key, market area key, call type key).
5.  **Data Loading (Partition Exchange)**: The aggregated data from the temporary table `TMP_SUBS_USAGE_MONTH_DET` is efficiently loaded into the corresponding partition of the permanent target table `ADM_SUBS_USAGE_MONTH_DET2` using an `ALTER TABLE ... EXCHANGE PARTITION` statement.
6.  **Statistics Gathering**: Finally, it gathers statistics on the newly loaded partition to ensure optimal query performance.

The overall purpose is to populate a partitioned data mart table with monthly detailed mobile subscription usage statistics, ensuring data quality and efficient loading processes.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.REL_SUBSCRIPTION]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_MONTH_DET]]
- → [[ADM_SUBS_USAGE_MONTH_DET2]]


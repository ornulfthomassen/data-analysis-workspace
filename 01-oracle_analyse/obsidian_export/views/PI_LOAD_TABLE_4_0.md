# PI_LOAD_TABLE_4_0

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and displays the most recent execution details (job name, status, start time, end time) for a specific set of ETL processes or data loads within the 'S_C_ALL' library. It identifies these processes by their 'etl_table' names, such as 'MOBILE_ORDER_DETAIL', 'FINANCE_SALES_REPORTING', various 'INSIGHT_SUBSCRIPTION' related loads, 'INSIGHT_CUSTOMER', and 'CHURN' related loads. For each specified 'etl_table', it retrieves the entry corresponding to the latest start time, effectively providing a snapshot of their most recent status.

## Data Sources (Inputs)
- ← [[ccm.ccm_daily_load]]


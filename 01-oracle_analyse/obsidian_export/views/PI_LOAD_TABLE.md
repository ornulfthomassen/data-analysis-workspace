# PI_LOAD_TABLE

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to display the latest (most recent start time) load status for a predefined set of specific ETL (Extract, Transform, Load) tables. It retrieves details such as the library, ETL table name, job name, job status, start time, and end time for the latest execution of these specified tables, primarily focusing on tables related to 'ORDER_DETAIL', 'FINANCE_SALES_REPORTING', and various 'INSIGHT' and 'CHURN' data products within the 'HDFS_CONS_PUBLIC' library.

## Data Sources (Inputs)
- ← [[ccm.ccm_daily_load]]


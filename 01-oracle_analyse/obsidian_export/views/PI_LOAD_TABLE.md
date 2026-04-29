# PI_LOAD_TABLE

**Schema:** `CCM` | **Type:** `View`

## Description
This view retrieves the latest load status entries for a specific set of ETL tables/processes from the `ccm_daily_load` log table. For each tracked ETL table (e.g., 'ORDER_DETAIL', 'FINANCE_SALES_REPORTING', various 'INSIGHT' related tables, and 'insight_churn_wide'), it identifies and returns the record with the most recent start time (`sttime`), including details such as the library, ETL table name, job name, job status, start time, and end time.

## Data Sources (Inputs)
- ← [[CCM.CCM_DAILY_LOAD]]
| Column Name |
|---|
| lib |
| etl_table |
| jobname |
| jobstat |
| sttime |
| endtime |


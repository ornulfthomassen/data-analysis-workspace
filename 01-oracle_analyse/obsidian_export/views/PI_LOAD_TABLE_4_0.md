# PI_LOAD_TABLE_4_0

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the latest load status (job name, status, start, and end times) for specific ETL processes (Mobile Order Detail, Finance Sales Reporting, Insight Subscription, Insight Customer, and Churn related processes) within the 'S_C_ALL' library. It identifies the most recent entry for each specified ETL table from the daily load tracking table.

## Data Sources (Inputs)
- ← [[ccm.ccm_daily_load]]
| Column Name |
|---|
| lib |
| etl_table |
| jobname |
| jobstat |
| sttime |
| endtime |


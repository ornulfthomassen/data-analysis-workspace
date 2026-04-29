# P_ADM_MINE_SIDER_DET_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure processes monthly weblog session and event detail data for a specified month (`P_YYYYMM`). It aggregates this data and loads it into a partitioned history table named `ADM_MINE_SIDER_DET_HIST`. The process involves validating source data, creating a new partition in the target table if it doesn't exist, populating a temporary table with the aggregated data, and then exchanging this temporary table with the corresponding partition in `ADM_MINE_SIDER_DET_HIST`. It includes error handling and logging mechanisms.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| FIRST_DATE |
| LAST_DATE |
| PERIOD_MONTH_KEY |
- ← [[WEBLOG.MICRO_LOG_SESSION]]
| Column Name |
|---|
| STARTING_TIME |
| KURT_ID |
| APPLICATION_ID |
| SESSION_ID |
- ← [[WEBLOG.MICRO_LOG]]
| Column Name |
|---|
| SESSION_ID |
| MICRO_LOG_ID |
| TIME |
| EVENT_TYPE_ID_MICRO_LOG |
- ← [[WEBLOG.MICRO_LOG_DETAIL]]
| Column Name |
|---|
| MICRO_LOG_ID |
| TIME |
| VALUE |
| EVENT_TYPE_ID_DETAIL |
- ← [[WEBLOG.EVENT_TYPE]]
| Column Name |
|---|
| EVENT_TYPE_ID |
| NAME |

## Target Tables (Outputs)
- → [[ADM_MINE_SIDER_DET_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| EVENT_NAME |
| EVENT_NAME_DETAIL |
| EVENT_VALUE |
| ANTALL_EVENTS |
| ANTALL_SESJONER |
| MIN_DATE |
| MAX_DATE |
- → [[TMP_MINE_SIDER_DET_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| EVENT_NAME |
| EVENT_NAME_DETAIL |
| EVENT_VALUE |
| ANTALL_EVENTS |
| ANTALL_SESJONER |
| MIN_DATE |
| MAX_DATE |


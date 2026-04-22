# P_ADM_MINE_SIDER_DET_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_MINE_SIDER_DET_HIST, processes web activity and session data for a specified month (P_YYYYMM) related to a 'My Pages' type application. It aggregates detailed user events and sessions from various WEBLOG tables into a temporary staging table. After aggregation, the data is loaded into a specific partition of the permanent historical administrative table ADM_MINE_SIDER_DET_HIST using a partition exchange mechanism. The procedure includes checks for source data availability, handles existing partitions (with an option to prevent overwrites), and includes error logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[WEBLOG.MICRO_LOG_SESSION]]
- ← [[WEBLOG.MICRO_LOG]]
- ← [[WEBLOG.MICRO_LOG_DETAIL]]
- ← [[WEBLOG.EVENT_TYPE]]

## Target Tables (Outputs)
- → [[TMP_MINE_SIDER_DET_HIST]]
- → [[ADM_MINE_SIDER_DET_HIST]]


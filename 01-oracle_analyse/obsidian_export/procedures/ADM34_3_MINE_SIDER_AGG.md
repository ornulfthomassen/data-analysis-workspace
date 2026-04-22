# ADM34_3_MINE_SIDER_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure, `ADM34_3_MINE_SIDER_AGG`, is designed to create and maintain a partitioned aggregate table named `CLM_ADM.ADM_MINE_SIDER_AGG`. Its primary purpose is to summarize user activity data (such as latest activity timestamp, total sessions, active sessions, failed sessions, and session details) for each `KURT_ID` (customer ID) on a 'Mine Sider' (My Pages) portal, aggregated by `PERIOD_MONTH_KEY`. The procedure processes data month by month within a specified date range. For each month, it dynamically manages partitions by dropping the existing partition for that month (if it exists) and then adding a new one. Finally, it populates the newly created partition with aggregated data derived from various source tables, including a reference to the aggregate table itself from the previous month. It also creates indexes and gathers statistics on the table after data insertion.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[CLM_ADM.ADM_MINE_SIDER]]
- ← [[CCM.ADM_MINE_SIDER_DET_HIST]]
- ← [[CCDW_WEBLOG.GETACCESS_CONSUMER_INFO]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MINE_SIDER_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MINE_SIDER_AGG]]


# ADM34_3_MINE_SIDER_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure aggregates 'Mine Sider' (My Pages) session statistics and user login data on a monthly basis, storing the results in a permanent, partitioned summary table named ADM_MINE_SIDER_AGG. It dynamically manages partitions (creating, dropping, and adding them for each processing month) and calculates metrics such as total sessions, active sessions, failed sessions, session details, and the latest activity timestamp for each user (KURT_ID) within the specified month range. It also handles the initial creation of the target table and its primary index if it does not already exist.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
- ← [[CLM_ADM.ADM_MINE_SIDER]]
| Column Name |
|---|
| KURT_ID |
| MAX_DTTM |
| NO_SESSIONS |
| NO_ACTIVE_SESSIONS |
| NO_FAILED_SESSIONS |
| PERIOD_MONTH_KEY |
- ← [[CCM.ADM_MINE_SIDER_DET_HIST]]
| Column Name |
|---|
| ANTALL_SESJONER |
| PERIOD_MONTH_KEY |
| KURT_ID |
- ← [[CCDW_WEBLOG.GETACCESS_CONSUMER_INFO]]
| Column Name |
|---|
| USER_DATE_LATEST_LOGGED_IN |
| KURT_ID |
| INFO_IS_DELETED |
- ← [[CLM_ADM.ADM_MINE_SIDER_AGG]]
| Column Name |
|---|
| KURT_ID |
| PERIOD_MONTH_KEY |
| MAX_DTTM |

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MINE_SIDER_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| MAX_DTTM |
| NO_SESSIONS |
| NO_ACTIVE_SESSIONS |
| NO_FAILED_SESSIONS |
| NO_SESSION_DETAILS |


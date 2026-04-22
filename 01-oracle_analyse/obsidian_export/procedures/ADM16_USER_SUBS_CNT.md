# ADM16_USER_SUBS_CNT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, ADM16_USER_SUBS_CNT, is designed to aggregate and load user subscription and activity data into a monthly partitioned summary table named `CRM_ANALYSE.ADM_USER_SUBS_CNT`. It checks for the existence of this target table and creates it with appropriate partitioning and indexes if it doesn't exist. The procedure then iterates through a specified range of months (determined by input parameters or system date), checks for missing data in source tables, and for each month, it either creates a new partition in the target table (if not already present) or inserts aggregated data from historical detail tables. It tracks the loading process by calling a separate load history procedure and manages table statistics and indexes for performance.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CRM_ANALYSE.ADM_SUBSCR_DETAIL_HIST]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[ADM_USER_SUBS_CNT]]


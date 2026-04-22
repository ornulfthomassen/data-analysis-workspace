# ADM19_1_MOB_SUBS_REVENUE_3MO

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure creates and populates a partitioned table named ADM_MOB_SUBS_REVENUE_3MO within the CRM_ANALYSE schema. Its main purpose is to calculate and store aggregated mobile subscription revenue data, adjusted for factors like roaming profit, over a three-month rolling period. It processes data month by month, dynamically creating new table partitions as needed for each period. The procedure also handles the initial creation of the target table, its indexes, and gathers statistics.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_MOB_SUBS_REVENUE]]
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]

## Target Tables (Outputs)
- → [[ADM_MOB_SUBS_REVENUE_3MO]]


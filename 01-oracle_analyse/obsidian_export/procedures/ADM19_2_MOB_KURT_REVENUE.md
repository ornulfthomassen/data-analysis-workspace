# ADM19_2_MOB_KURT_REVENUE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure `ADM19_2_MOB_KURT_REVENUE` is responsible for aggregating monthly mobile subscription revenue data. It creates two permanent partitioned tables, `CRM_ANALYSE.ADM_MOB_KURT_OWNER_REVENUE_3MO` and `CRM_ANALYSE.ADM_MOB_KURT_USER_REVENUE_3MO`, if they do not exist. For a specified range of months (defaulting to the previous month if not provided), it iterates through each month. For each month, it checks if corresponding data already exists in the target tables. If not, it dynamically adds a new partition for that month to the respective table and inserts aggregated revenue data. The aggregation is done from `CRM_ANALYSE.ADM_MOB_SUBS_REVENUE_3MO`, grouping by 'owner' for one table and 'user' for the other. It also manages table statistics and logs operational history.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_MOB_SUBS_REVENUE_3MO]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_MOB_KURT_OWNER_REVENUE_3MO]]
- → [[CRM_ANALYSE.ADM_MOB_KURT_USER_REVENUE_3MO]]


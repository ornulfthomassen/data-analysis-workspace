# P_ADM_MOB_SUBS_REVENUE_3MO

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and loads mobile subscription revenue data for a specified period (defaulting to the previous month) into a partitioned data warehouse table, ADM_MOB_SUBS_REVENUE_3MO. It first aggregates detailed subscription revenue data for a 3-month rolling window (hence '3MO') from CLM_ADM.ADM_MOB_SUBS_REVENUE into a temporary staging table, TMP_MOB_SUBS_REVENUE_3MO. The aggregation includes various revenue components, applies revenue adjustments (e.g., based on active days and roaming factors), and groups by subscription details. After creating and populating the temporary table, it then creates a new partition (if it doesn't exist) in the target ADM_MOB_SUBS_REVENUE_3MO table for the specific period and exchanges the data from the temporary table into this new partition. The procedure includes robust error handling, checks for source data availability, manages partition existence, gathers statistics for the new partition, and logs its activities.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_MOB_SUBS_REVENUE_3MO]]
- → [[ADM_MOB_SUBS_REVENUE_3MO]]


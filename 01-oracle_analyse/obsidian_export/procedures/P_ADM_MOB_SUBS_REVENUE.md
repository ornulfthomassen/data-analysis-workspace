# P_ADM_MOB_SUBS_REVENUE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates mobile subscription revenue data for a specified period (month/year). It processes raw subscription details, fees, and usage (including roaming) data from various source systems, stores intermediate results in several temporary tables, and finally loads the consolidated revenue figures into a permanent, partitioned administrative table. It includes checks for the availability of source data and manages partitions in the target table.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[STLOG.ST_AGG]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
- ← [[CCDW_USAGE.MOBILE_ROAMING_DAILY]]

## Target Tables (Outputs)
- → [[TMP_MOB_SUBS_REVENUE_SUBS]]
- → [[TMP_MOB_SUBS_REVENUE_FEE]]
- → [[TMP_MOB_SUBS_REVENUE_USE]]
- → [[TMP_MOB_SUBS_REVENUE_USE_ROAM]]
- → [[TMP_MOB_SUBS_REVENUE]]
- → [[ADM_MOB_SUBS_REVENUE]]


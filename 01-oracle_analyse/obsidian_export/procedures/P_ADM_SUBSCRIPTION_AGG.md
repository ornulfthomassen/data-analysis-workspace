# P_ADM_SUBSCRIPTION_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure calculates and aggregates subscription-related metrics (such as data usage, MMS, SMS, voice activity, and associated revenue from fees and usage) for a specified month and the two preceding months. It collects data from various source systems, stages it in a temporary table, and then loads this aggregated data into a specific monthly partition of the permanent 'ADM_SUBSCRIPTION_AGG' table. It includes robust checks for source data availability and existing partition data to ensure data integrity and prevent accidental overwrites.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[STLOG.ST_AGG]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_AGG]]
- → [[TMP_SUBSCRIPTION_AGG]]


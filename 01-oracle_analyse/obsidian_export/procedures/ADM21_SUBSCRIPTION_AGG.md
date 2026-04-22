# ADM21_SUBSCRIPTION_AGG

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Aggregates monthly subscription usage (mobile data, MMS, SMS, voice) and revenue data from various source tables into a partitioned target table `CRM_ANALYSE.ADM_SUBSCRIPTION_AGG`. The procedure dynamically creates the target table and its monthly partitions if they do not exist, manages indexes, and iteratively processes data for a specified range of months, performing availability checks on source data before insertion.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CRM_ANALYSE.TMP_TRAFFIC_DATA]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[STLOG.ST_AGG]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCRIPTION_AGG]]


# P_ADM_MOBILE_TRAFFIC_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, P_ADM_MOBILE_TRAFFIC_AGG, aggregates mobile traffic data for a specified month (P_YYYYMM). It performs initial checks on data readiness and target table/partition existence. It then creates two intermediate, temporary tables (TMP1_MOBILE_TRAFFIC_AGG and TMP2_MOBILE_TRAFFIC_AGG) by selecting and joining data from various source systems, performing aggregations. Finally, it loads the processed data from the second temporary table (TMP2_MOBILE_TRAFFIC_AGG) into a partition of the main target table (ADM_MOBILE_TRAFFIC_AGG) using an EXCHANGE PARTITION operation, ensuring efficient data loading for partitioned tables. It also manages partition creation, index rebuilding, and statistics collection, logging all actions and handling errors.

## Data Sources (Inputs)
- ← [[CDR.CDR_GENEVA]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]

## Target Tables (Outputs)
- → [[TMP1_MOBILE_TRAFFIC_AGG]]
- → [[TMP2_MOBILE_TRAFFIC_AGG]]
- → [[ADM_MOBILE_TRAFFIC_AGG]]


# P_ADM_SUBSCRIPTION_AGG_I

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_SUBSCRIPTION_AGG_I`, aggregates various subscription-related metrics (such as data usage, MMS, SMS, voice duration/count, and corresponding revenues) for a specified month (`P_YYYYMM`). It performs a preliminary check to ensure all necessary source data tables/views are complete for the given month. If the data is available, it calculates the aggregated metrics, stores them in a temporary staging table (`TMP_SUBSCRIPTION_AGG_I`), and then efficiently loads this data into a specific monthly partition of the main analytical table (`ADM_SUBSCRIPTION_AGG_I`) using an `ALTER TABLE ... EXCHANGE PARTITION` operation. The procedure also handles the creation of new partitions if they don't exist and manages checks to prevent overwriting existing data without explicit permission.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[GALAXY.TRAFFIC_MONTH_FACT_V]]
- ← [[GALAXY.SUBSCR_FEE_MONTH_FACT_V]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[STLOG.ST_AGG]]

## Target Tables (Outputs)
- → [[TMP_SUBSCRIPTION_AGG_I]]
- → [[ADM_SUBSCRIPTION_AGG_I]]


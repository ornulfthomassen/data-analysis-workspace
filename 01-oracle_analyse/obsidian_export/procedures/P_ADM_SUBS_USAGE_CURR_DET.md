# P_ADM_SUBS_USAGE_CURR_DET

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure calculates and aggregates current monthly subscription usage details. It creates a temporary staging table, populates it with detailed usage data from various fact and dimension tables (filtered for the current month), applies `NOT NULL` constraints, and then loads this aggregated data into a specific partition of a permanent analytical table (`ADM_SUBS_USAGE_MONTH_DET`) by performing an `ALTER TABLE ... EXCHANGE PARTITION` operation. It handles partition creation if necessary and gathers statistics on the newly loaded partition. Error handling and logging are also included.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_CURR_DET]]
- → [[ADM_SUBS_USAGE_MONTH_DET]]


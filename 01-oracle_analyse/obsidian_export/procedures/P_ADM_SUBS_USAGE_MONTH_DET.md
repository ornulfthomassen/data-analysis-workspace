# P_ADM_SUBS_USAGE_MONTH_DET

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_SUBS_USAGE_MONTH_DET`, is designed to process and aggregate mobile subscription usage data on a monthly basis. It first performs checks for the availability of source data for the specified month. If data sources are complete, it dynamically creates a temporary table (`TMP_SUBS_USAGE_MONTH_DET`) where it aggregates detailed daily usage facts from `GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V`. The aggregation includes summing various financial amounts, usage volumes, and event counts, along with complex logic to determine subscription and sub-number relationships. After populating the temporary table, it manages partitions for the permanent target table (`ADM_SUBS_USAGE_MONTH_DET`), adding a new partition if it doesn't exist for the specified month. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` operation to efficiently move the aggregated data from the temporary table into the corresponding partition of the permanent `ADM_SUBS_USAGE_MONTH_DET` table. The procedure includes robust error handling and logging mechanisms.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_SUBS_USAGE_MONTH_DET]]
- → [[CLM_ADM.ADM_SUBS_USAGE_MONTH_DET]]


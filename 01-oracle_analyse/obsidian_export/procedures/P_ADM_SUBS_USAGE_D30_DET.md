# P_ADM_SUBS_USAGE_D30_DET

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates subscription usage data for a 30-day period. It first creates a temporary staging table ('TMP_SUBS_USAGE_D30_DET') with the aggregated results. Subsequently, it performs an 'EXCHANGE PARTITION' operation to move the data from this temporary table into a specific partition of the permanent administrative table ('ADM_SUBS_USAGE_MONTH_DET'), effectively updating the main usage detail table. It also manages partition creation and gathers statistics.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCR_USAGE_MOBILE_DAY_FACT_V]]

## Target Tables (Outputs)
- → [[TMP_SUBS_USAGE_D30_DET]]
- → [[ADM_SUBS_USAGE_MONTH_DET]]


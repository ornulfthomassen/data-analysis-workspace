# P_EXT_CHURN_AGRMT_REWARD

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_EXT_CHURN_AGRMT_REWARD` extracts and processes churn-related agreement reward data. It first stages detailed reward information from a source view into a temporary table, then filters and deduplicates this data, separating distinct records from any duplicates. It enriches the distinct records by joining with an aggregated bonus view. Finally, it calculates various churn activation/deactivation and qualification/dequalification flags for agreements based on the historical trend of reward units using analytic functions, storing all intermediate and final results in temporary tables.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[ALL_OBJECTS]]
- ← [[CLM_ADM.CHURN_ADM_AGRMT_FAMILIEBONUS_DET_V]]
- ← [[CLM_ADM.CHURN_ADM_AGRMT_FAMILIEBONUS_AGG_V]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CHURN_ADM_AGRMT_FAMILIEBONUS_DET]]
- → [[CLM_ADM.TMP_CHURN_CP_FB_DETAIL]]
- → [[CLM_ADM.TMP_CHURN_CP_FB_DETAIL_DUP]]
- → [[CLM_ADM.TMP_CHURN_CP_FB_DETAIL_WITH_AGGR]]
- → [[CLM_ADM.TMP_CHURN_AGRMT_REWARD]]


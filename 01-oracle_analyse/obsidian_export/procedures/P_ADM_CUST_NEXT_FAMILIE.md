# P_ADM_CUST_NEXT_FAMILIE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Calculates monthly aggregated counts of specific 'Next Family' product offers (categorized by adult vs. under 18) per customer. It uses subscription history and a month dimension for aggregation. The results are staged in a temporary table, then loaded into a specific partition of a permanent aggregate table via partition exchange. The procedure includes checks for source data availability and target table/partition existence, along with comprehensive error handling.

## Data Sources (Inputs)
- ← [[ADM_SUBS_NEXT_FAMILIE_AGG]]
- ← [[ADM_SUBSCRIPTION_HISTORY]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]

## Target Tables (Outputs)
- → [[TMP_CUST_NEXT_FAMILIE_AGG]]
- → [[ADM_CUST_NEXT_FAMILIE_AGG]]


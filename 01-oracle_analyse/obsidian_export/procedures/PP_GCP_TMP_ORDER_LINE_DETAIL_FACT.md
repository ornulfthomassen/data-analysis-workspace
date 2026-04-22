# PP_GCP_TMP_ORDER_LINE_DETAIL_FACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `PP_GCP_TMP_ORDER_LINE_DETAIL_FACT` dynamically creates or recreates a temporary staging table named `TMP_ORDER_LINE_DETAIL_FACT`. This table is populated with order line detail data from a specified source table (`P_SOURCE_TABLE`), filtered by a period month key (`P_PERIOD_MONTH_KEY`) and specific system keys or order statuses depending on the `P_SOURCE` parameter. After creation, it ensures a unique index exists on the temporary table (dropping and recreating if necessary) and gathers statistics for performance optimization. This procedure appears to be a data preparation step for subsequent processing of order line details.

## Data Sources (Inputs)
- ← [[P_SOURCE_TABLE]]

## Target Tables (Outputs)
- → [[TMP_ORDER_LINE_DETAIL_FACT]]


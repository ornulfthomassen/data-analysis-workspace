# PP_GCP_TMP_ORDER_LINE_DETAIL_FACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `PP_GCP_TMP_ORDER_LINE_DETAIL_FACT` dynamically creates and populates a temporary order line detail fact table named `TMP_ORDER_LINE_DETAIL_FACT`. It filters data from a source table (specified by `P_SOURCE_TABLE`) based on the `P_SOURCE` parameter and `P_PERIOD_MONTH_KEY`. It adds new `PERIOD_MONTH_KEY` and `ORDER_SOURCE` columns, creates a unique index on specific columns (including `ORDER_LINE_KEY` from the source), and gathers statistics on the newly created table. The table is dropped and recreated on each execution, serving as an intermediate dataset.

## Data Sources (Inputs)
- ← [[<P_SOURCE_TABLE_PARAM>]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| ORDER_DATE_KEY |
| ORDER_STATUS_KEY |
| ORDER_STATUS_DATE_KEY |
| ORDER_LINE_KEY |

## Target Tables (Outputs)
- → [[TMP_ORDER_LINE_DETAIL_FACT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| ORDER_SOURCE |
| ORDER_LINE_KEY |


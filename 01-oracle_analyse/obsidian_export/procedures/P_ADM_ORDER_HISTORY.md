# P_ADM_ORDER_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_ORDER_HISTORY` processes detailed order line facts for a specified month (`P_YYYYMM`). It performs an initial aggregation of order details, product information, and customer mappings to populate a partitioned `ADM_ORDER_HISTORY` table. Subsequently, it uses the newly generated `ADM_ORDER_HISTORY` data, along with product dimensions, to calculate and store aggregated data package usage metrics into three additional monthly partitioned history tables: `ADM_DATAPAKKE_HISTORY_OWNER` (aggregated by customer owner), `ADM_DATAPAKKE_HISTORY_USER` (aggregated by customer user), and `ADM_DATAPAKKE_HISTORY_SUBS` (aggregated by subscription ID). The process involves creating temporary tables, populating them with the aggregated data, and then exchanging these temporary tables with partitions of the permanent target tables.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[ADM_ORDER_HISTORY]]

## Target Tables (Outputs)
- → [[ADM_ORDER_HISTORY]]
- → [[TMP_ORDER_HISTORY]]
- → [[ADM_DATAPAKKE_HISTORY_OWNER]]
- → [[TMP_DATAPAKKE_HISTORY_OWNER]]
- → [[ADM_DATAPAKKE_HISTORY_USER]]
- → [[TMP_DATAPAKKE_HISTORY_USER]]
- → [[ADM_DATAPAKKE_HISTORY_SUBS]]
- → [[TMP_DATAPAKKE_HISTORY_SUBS]]


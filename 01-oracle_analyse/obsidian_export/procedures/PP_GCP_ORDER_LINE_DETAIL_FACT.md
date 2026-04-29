# PP_GCP_ORDER_LINE_DETAIL_FACT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Manages and loads data into monthly partitions and subpartitions (AO, SO, FT, HW, NB) of the 'GCP_ORDER_LINE_DETAIL_FACT' table. It uses a staging table ('TMP_ORDER_LINE_DETAIL_FACT') and a partition exchange mechanism to efficiently update subpartitions with data primarily sourced from various 'CCM.VYA_ORDER_LINE_DETAIL_FACT' tables, for a specified range of months.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| YEAR_MONTH_NUMBER |
- ← [[DUAL]]
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT]]
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_FT]]
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_HW]]
- ← [[CCM.VYA_ORDER_LINE_DETAIL_FACT_NB]]
- ← [[TMP_ORDER_LINE_DETAIL_FACT]]

## Target Tables (Outputs)
- → [[GCP_ORDER_LINE_DETAIL_FACT]]
- → [[TMP_ORDER_LINE_DETAIL_FACT]]


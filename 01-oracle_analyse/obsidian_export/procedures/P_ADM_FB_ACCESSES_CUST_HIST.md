# P_ADM_FB_ACCESSES_CUST_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure populates a monthly partition of the `ADM_FB_ACCESSES_CUST_HIST` table with fixed broadband access and customer history data. It performs checks for source data availability and existing partitions for a given month (`P_YYYYMM`). Data is first loaded into a temporary staging table (`TMP_FB_ACCESSES_CUST_HIST`), and then this temporary table's data segment is efficiently swapped into the corresponding partition of the permanent `ADM_FB_ACCESSES_CUST_HIST` table using an `ALTER TABLE ... EXCHANGE PARTITION` command. It also rebuilds indexes and collects statistics on the newly loaded partition.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[AGR.BMGM_ACCESSES_KURT]]
- ← [[STLOG.ST_IN]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CM.AGREEMENT_OFFER]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]

## Target Tables (Outputs)
- → [[TMP_FB_ACCESSES_CUST_HIST]]
- → [[ADM_FB_ACCESSES_CUST_HIST]]


# P_ADM_FB_COUNTS_CUST_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates fixed broadband and telephony product counts for customers on a monthly basis. It processes data from various source tables, validates the availability of source data, and then creates a temporary table to hold these aggregated counts. Subsequently, it uses this temporary table to exchange (update or add) a specific partition in a permanent historical administrative table (`ADM_FB_COUNTS_CUST_HIST`). The procedure includes logic for handling partition existence, adding new partitions if needed, rebuilding local indexes, and collecting statistics after the partition exchange. It also incorporates error handling and logging of procedure status.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[AGR.BMGM_COUNTS_KURT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- ← [[ADM_FB_COUNTS_CUST_HIST]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[STLOG.ST_IN]]

## Target Tables (Outputs)
- → [[ADM_FB_COUNTS_CUST_HIST]]
- → [[TMP_FB_COUNTS_CUST_HIST]]


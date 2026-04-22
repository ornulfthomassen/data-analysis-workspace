# STOCK_FTV_HISTORY_TV

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `STOCK_FTV_HISTORY_TV` is designed to process and aggregate daily TV subscription and agreement history data. It performs the following main steps:
1.  **Extracts Raw Agreement Data:** It retrieves agreement details from the `KAS` schema (tables like `AVTALE`, `KUNDE`, `MARKEDSAVTALE_RESSURS`, `MARKEDSAVTALE`), filtering by status, dates, and product numbers, and stores this in a temporary raw table (`TMP_STOCK_FTV_HIST_TVAGREE_RAW`).
2.  **Extracts Raw Subscription Data:** It pulls subscribed product information from `CCDW.SUBSCRIBED_PRODUCT` and various `GALAXY` dimension tables (like `DATE_DIM_MV`, `SUBSCRIPTION`, `PRODUCT_DIM`, `SUBSCRIPTION_DIM_MV`), filtering by dates and product offer IDs, and aggregates initial counts. This data is stored in another temporary raw table (`TMP_STOCK_FTV_HIST_TVSTOCK_RAW`).
3.  **Enriches Raw Data (Problematic Section):** A section intended to 'add segments' attempts to create `TMP_STOCK_FTV_HIST_TV_RAW`. The SQL statement for this step is malformed/incomplete in the provided script, as it attempts to use `V_TABLE_RAW` (the target table) as a source within its own `CREATE TABLE AS SELECT` statement (`FROM '||V_TABLE_RAW||' BAL`). It also references `V_TABLE_A_RAW` and joins with several dimension tables (`GALAXY.DATE_DIM_MV`, `CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V`, `GALAXY.CUSTOMER_DIM`, `CRM_ANALYSE.LIVSFASESEGMENT_MOBILE`, `W_DUAL_PLAY`) to enrich the data with customer demographics and segmentation information.
4.  **Aggregates Detailed Data:** Finally, it aggregates data from `STOCK_FTV_HISTORY_TV_DET` (a table that is used as a source but whose creation is not explicitly shown in the provided script fragment) into a summary aggregate table (`STOCK_FTV_HISTORY_TV_AGG`). The aggregation includes sums (`BALANCE`), refresh dates, various period keys, customer age, customer types, segment IDs, and product keys. All created tables are temporary, being dropped and recreated during each execution of the procedure.

## Data Sources (Inputs)
- ← [[KAS.AVTALE]]
- ← [[KAS.KUNDE]]
- ← [[KAS.MARKEDSAVTALE_RESSURS]]
- ← [[KAS.MARKEDSAVTALE]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE]]
- ← [[W_DUAL_PLAY]]
- ← [[TMP_STOCK_FTV_HIST_TVAGREE_RAW]]
- ← [[TMP_STOCK_FTV_HIST_TV_RAW]]
- ← [[STOCK_FTV_HISTORY_TV_DET]]

## Target Tables (Outputs)
- → [[TMP_STOCK_FTV_HIST_TVAGREE_RAW]]
- → [[TMP_STOCK_FTV_HIST_TVSTOCK_RAW]]
- → [[TMP_STOCK_FTV_HIST_TV_RAW]]
- → [[STOCK_FTV_HISTORY_TV_AGG]]


# STOCK_FTV_HISTORY_TEST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The main functionality of this procedure is to orchestrate the extraction and staging of raw, detailed subscription history data for a specific date. It dynamically creates and schedules a sub-procedure (`ASYNC_PROC_KAS`) which, in turn, creates a new table (`TMP_STOCK_FTV_HIST_RAW_KAS`). This table is populated with subscription details from various GALAXY schema tables/views, filtered for specific product categories (Bredbånd, Frihet, TV subscriptions) associated with the 'KAS' source system. The overall process appears to be a step in building a detailed and aggregated history for fixed-telephony/TV ('FTV') services.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]

## Target Tables (Outputs)
- → [[TMP_STOCK_FTV_HIST_RAW_KAS]]


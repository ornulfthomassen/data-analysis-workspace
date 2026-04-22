# STOCK_FTV_HISTORY

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `STOCK_FTV_HISTORY` processes and consolidates historical subscription data from various source systems (KAS, Lumino, TBB, etc.) for a specified date. It constructs several temporary tables to filter and enrich the data with customer demographics, location information, product details, and dual-play indicators. The primary goal is to generate a detailed subscription history table (`STOCK_FTV_HISTORY_DET`) and subsequently an aggregated summary table (`STOCK_FTV_HISTORY_AGG`) related to 'Stock FTV' (Fiber-to-the-X) subscriptions, presumably for analytical purposes.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[LIVE.SUBSCRIPTION_HANDSET_HIST]]
- ← [[GALAXY.LOCATION_DIM]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
- ← [[GALAXY.CUSTOMER_DIM]]
- ← [[CRM_ANALYSE.LIVSFASESEGMENT_MOBILE]]

## Target Tables (Outputs)
- → [[TMP_STOCK_FTV_HISTORY_RAW_KAS]]
- → [[TMP_STOCK_FTV_HISTORY_RAW_LUM]]
- → [[TMP_STOCK_FTV_HISTORY_RAW_TBB]]
- → [[TMP_STOCK_FTV_HISTORY_RAW_DP]]
- → [[TMP_STOCK_FTV_ACTIVATION]]
- → [[STOCK_FTV_HISTORY_DET]]
- → [[STOCK_FTV_HISTORY_AGG]]


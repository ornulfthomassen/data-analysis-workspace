# P_RELOAD_FTV_STOCK_BASE_V2

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure performs a two-step data refresh for stock base information. It first truncates and reloads a temporary/staging table (CCM.FTV_STOCK_BASE_V2_TMP) using data from a source view (CCM.FTV_STOCK_BASE_V2_V). Subsequently, it truncates and reloads the main stock base table (CCM.FTV_STOCK_BASE_V2) using the data from the previously populated temporary staging table.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_BASE_V2_V]]
- ← [[CCM.FTV_STOCK_BASE_V2_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_STOCK_BASE_V2_TMP]]
- → [[CCM.FTV_STOCK_BASE_V2]]


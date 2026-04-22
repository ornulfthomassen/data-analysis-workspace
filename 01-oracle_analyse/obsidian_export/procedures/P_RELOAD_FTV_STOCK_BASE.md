# P_RELOAD_FTV_STOCK_BASE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_RELOAD_FTV_STOCK_BASE` is designed to completely reload the `CCM.FTV_STOCK_BASE` table. It achieves this by first clearing and repopulating a temporary/staging table, `CCM.FTV_STOCK_BASE_TMP`, with data sourced from `CCM.FTV_STOCK_BASE_V`. Subsequently, it clears and repopulates the final `CCM.FTV_STOCK_BASE` table using the data from the `CCM.FTV_STOCK_BASE_TMP` table.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_BASE_V]]
- ← [[CCM.FTV_STOCK_BASE_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_STOCK_BASE_TMP]]
- → [[CCM.FTV_STOCK_BASE]]


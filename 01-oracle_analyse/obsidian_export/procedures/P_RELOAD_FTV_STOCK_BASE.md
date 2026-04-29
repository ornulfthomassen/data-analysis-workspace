# P_RELOAD_FTV_STOCK_BASE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Reloads the FTV_STOCK_BASE table by first populating an intermediate temporary table (FTV_STOCK_BASE_TMP) from a view (FTV_STOCK_BASE_V), and then transferring the data from the temporary table to the main FTV_STOCK_BASE table.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_BASE_V]]
- ← [[CCM.FTV_STOCK_BASE_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_STOCK_BASE_TMP]]
- → [[CCM.FTV_STOCK_BASE]]


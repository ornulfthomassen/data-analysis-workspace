# P_RELOAD_FTV_STOCK_BASE_V2

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Refreshes the 'FTV_STOCK_BASE_V2' table. It first clears and reloads a temporary table 'FTV_STOCK_BASE_V2_TMP' with data from the 'FTV_STOCK_BASE_V2_V' view, and then uses this temporary table to clear and reload the main 'FTV_STOCK_BASE_V2' table.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_BASE_V2_V]]
- ← [[CCM.FTV_STOCK_BASE_V2_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_STOCK_BASE_V2_TMP]]
- → [[CCM.FTV_STOCK_BASE_V2]]


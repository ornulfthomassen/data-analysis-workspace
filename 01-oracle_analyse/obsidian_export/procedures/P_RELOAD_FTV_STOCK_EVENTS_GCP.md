# P_RELOAD_FTV_STOCK_EVENTS_GCP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure reloads the `FTV_STOCK_EVENTS_GCP` table by first populating a temporary staging table `FTV_STOCK_EVENTS_GCP_TMP` from the `FTV_STOCK_EVENTS_V` view, and then transferring the data from the staging table to the final `FTV_STOCK_EVENTS_GCP` table. Both target tables are fully refreshed with `DELETE` and `INSERT` operations.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_EVENTS_V]]
- ← [[CCM.FTV_STOCK_EVENTS_GCP_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_STOCK_EVENTS_GCP_TMP]]
- → [[CCM.FTV_STOCK_EVENTS_GCP]]


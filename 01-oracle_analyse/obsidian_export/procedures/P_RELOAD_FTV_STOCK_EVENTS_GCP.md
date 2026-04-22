# P_RELOAD_FTV_STOCK_EVENTS_GCP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure reloads stock event data by performing a two-step synchronization. First, it clears all data from the staging table `CCM.FTV_STOCK_EVENTS_GCP_TMP` and populates it with fresh data from the source view `CCM.FTV_STOCK_EVENTS_V`. Second, it clears all data from the main target table `CCM.FTV_STOCK_EVENTS_GCP` and then populates it with the data from the newly reloaded staging table `CCM.FTV_STOCK_EVENTS_GCP_TMP`.

## Data Sources (Inputs)
- ← [[CCM.FTV_STOCK_EVENTS_V]]
- ← [[CCM.FTV_STOCK_EVENTS_GCP_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_STOCK_EVENTS_GCP_TMP]]
- → [[CCM.FTV_STOCK_EVENTS_GCP]]


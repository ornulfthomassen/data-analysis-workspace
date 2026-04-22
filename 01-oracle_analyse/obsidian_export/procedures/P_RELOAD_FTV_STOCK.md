# P_RELOAD_FTV_STOCK

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure, `P_RELOAD_FTV_STOCK`, acts as an orchestrator for refreshing or reloading various aspects of stock-related data, likely for a Fact Table View (FTV) system. It sequentially calls several sub-procedures within the `CCM` schema: `P_RELOAD_FTV_STOCK_BASE_V2`, `P_RELOAD_FTV_LOCATION_EVENTS_GCP`, `P_RELOAD_FTV_STOCK_EVENTS_GCP`, and `P_RELOAD_FTV_STOCK_BASE`. These sub-procedures are presumably responsible for handling specific data reloading tasks, potentially involving base stock data and events related to stock movement or location, possibly with integration or sourcing from Google Cloud Platform (GCP). The procedure also logs timestamps at different stages using `dbms_output.put_line` for monitoring execution progress.


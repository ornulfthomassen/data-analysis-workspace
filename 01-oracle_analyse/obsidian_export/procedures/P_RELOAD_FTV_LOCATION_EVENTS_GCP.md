# P_RELOAD_FTV_LOCATION_EVENTS_GCP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure `P_RELOAD_FTV_LOCATION_EVENTS_GCP` performs a two-stage data reload process. It first clears the `CCM.FTV_LOCATION_EVENTS_GCP_TMP` table (which acts as a staging area) and populates it with data extracted from the `CCM.FTV_LOCATION_EVENTS_V` view. Following this, it clears the main `CCM.FTV_LOCATION_EVENTS_GCP` table and populates it with the data from the `CCM.FTV_LOCATION_EVENTS_GCP_TMP` staging table. Essentially, it refreshes the `CCM.FTV_LOCATION_EVENTS_GCP` table using `CCM.FTV_LOCATION_EVENTS_V` as the source, via an intermediate staging table.

## Data Sources (Inputs)
- ← [[CCM.FTV_LOCATION_EVENTS_V]]
- ← [[CCM.FTV_LOCATION_EVENTS_GCP_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_LOCATION_EVENTS_GCP]]
- → [[CCM.FTV_LOCATION_EVENTS_GCP_TMP]]


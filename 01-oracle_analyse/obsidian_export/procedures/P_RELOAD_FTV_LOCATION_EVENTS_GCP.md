# P_RELOAD_FTV_LOCATION_EVENTS_GCP

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Performs a full reload of the `CCM.FTV_LOCATION_EVENTS_GCP` table by first populating an intermediate temporary table `CCM.FTV_LOCATION_EVENTS_GCP_TMP` from the `CCM.FTV_LOCATION_EVENTS_V` view, and then transferring the data from the temporary table to the final target table.

## Data Sources (Inputs)
- ← [[CCM.FTV_LOCATION_EVENTS_V]]
- ← [[CCM.FTV_LOCATION_EVENTS_GCP_TMP]]

## Target Tables (Outputs)
- → [[CCM.FTV_LOCATION_EVENTS_GCP_TMP]]
- → [[CCM.FTV_LOCATION_EVENTS_GCP]]


# ADM20_MOBILE_TRAFFIC_AGG1

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `ADM20_MOBILE_TRAFFIC_AGG1` is designed to aggregate mobile traffic data on a monthly basis. It processes call detail records (CDR) from the `CDR.CDR_GENEVA` table, performs various aggregations and calculations, and then loads this summarized data into a permanent, partitioned aggregate table named `CLM_ADM.ADM_MOBILE_TRAFFIC_AGG1`. The procedure handles the initial creation of the main aggregate table if it doesn't exist, as well as the creation of new monthly partitions within it. For loading data, it utilizes a temporary staging table (`CLM_ADM.TMP_MOBILE_TRAFFIC_AGG1`) and an `EXCHANGE PARTITION` operation for efficient and atomic data insertion into the target partition. It also includes checks for the readiness and completeness of the source data and prevents reprocessing of already loaded months.

## Data Sources (Inputs)
- ← [[CDR.CDR_GENEVA]]
- ← [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG1]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG1]]
- → [[CLM_ADM.TMP_MOBILE_TRAFFIC_AGG1]]


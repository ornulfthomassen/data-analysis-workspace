# P_ADM_YNG_MUSIC_FREEDOM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure is designed to load aggregated mobile traffic data, specifically for 'Music Freedom' (identified by APN '199'), for a given month (P_YYYYMM parameter) into a partitioned analytics table named ADM_YNG_MUSIC_FREEDOM. The process involves several steps: checking the availability and integrity of source data, managing partitions in the target table (adding a new partition if it doesn't exist), creating a temporary staging table (TMP_YNG_MUSIC_FREEDOM) to calculate and hold the aggregated data, and finally, using a partition exchange operation to efficiently load the data from the temporary table into the corresponding partition of the permanent ADM_YNG_MUSIC_FREEDOM table. The procedure also includes error handling and logging mechanisms.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_MOBILE_TRAFFIC_AGG]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[ADM_YNG_MUSIC_FREEDOM]]

## Target Tables (Outputs)
- → [[ADM_YNG_MUSIC_FREEDOM]]
- → [[TMP_YNG_MUSIC_FREEDOM]]


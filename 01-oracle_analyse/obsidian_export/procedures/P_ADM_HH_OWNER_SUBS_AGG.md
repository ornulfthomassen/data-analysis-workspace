# P_ADM_HH_OWNER_SUBS_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_HH_OWNER_SUBS_AGG` aggregates customer subscription and traffic data at the household level for a specific month (`V_YYYYMM`). It calculates various metrics such as gross/net fees, usage, subscription counts for different services (MPP, MPR, MBB, FIX, DSL, FBR, TNM, DJU), and related activity days and traffic volumes (MB, KR, MMS, SMS, Voice). This aggregated data is initially stored in a temporary table (`TMP_HH_OWNER_SUBS_AGG`). Subsequently, it uses an `ALTER TABLE ... EXCHANGE PARTITION` operation to efficiently load this data into a monthly partition of the permanent target table `ADM_HH_OWNER_SUBS_AGG`. The procedure includes robust error handling for non-existent tables, missing source data, and attempts to overwrite existing partitions.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[ADM_HH_OWNER_SUBS_AGG]]

## Target Tables (Outputs)
- → [[TMP_HH_OWNER_SUBS_AGG]]
- → [[ADM_HH_OWNER_SUBS_AGG]]


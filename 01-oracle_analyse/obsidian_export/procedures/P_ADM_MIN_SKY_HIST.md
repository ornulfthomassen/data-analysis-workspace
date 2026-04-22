# P_ADM_MIN_SKY_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Automates the historical data loading process for 'MIN_SKY' data. For a given month (`P_YYYYMM`), it first validates the integrity and completeness of source data from `COMOYO.MINSKY_MAIN_DAILY` and `COMOYO.MINSKY_DEVICES_DAILY`. It then extracts, aggregates, and transforms various metrics related to user activity and device usage from these sources, along with month-dimension information, into a temporary staging table. Finally, it loads this processed data into a specific partition (identified by the month `P_YYYYMM`) of the permanent historical table `ADM_MIN_SKY_HIST` by either creating a new partition or overwriting an existing one, utilizing an `EXCHANGE PARTITION` operation for efficient data loading.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[COMOYO.MINSKY_MAIN_DAILY]]
- ← [[COMOYO.MINSKY_DEVICES_DAILY]]

## Target Tables (Outputs)
- → [[ADM_MIN_SKY_HIST]]
- → [[TMP_MIN_SKY_HIST]]


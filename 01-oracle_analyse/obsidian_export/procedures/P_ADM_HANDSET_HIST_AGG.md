# P_ADM_HANDSET_HIST_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure aggregates historical handset usage data from the `CLM_ADM.ADM_SUBSCR_HANDSET_HIST_AGG` table. It groups the data by `MODELID` and calculates the count of entries, along with the minimum and maximum values for various period keys, terminal usage dates, producer names, model names, device OS types, categories, touch screen status, device types, HD voice, and LTE capabilities. Before processing, it performs a check to ensure sufficient data exists in both the main source table (`CLM_ADM.ADM_SUBSCR_HANDSET_HIST_AGG`) and `GALAXY.DATE_DIM_MV` for the specified month. If the target aggregated table (`ADM_HANDSET_HIST_AGG`) already exists, it is dropped and then recreated, effectively performing a full overwrite. After creation, statistics are computed on the new table, and `SELECT` privileges are granted to `CRM_ANALYSE`.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST_AGG]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_HANDSET_HIST_AGG]]

